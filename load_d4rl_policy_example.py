# python3
# Copyright 2020 Google LLC.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Loading a policy snapshot example."""

import json
import os
import pickle
import pprint

from absl import app
from absl import flags
import d4rl  # pylint:disable=unused-import
import gym
import numpy as np
import tensorflow as tf

flags.DEFINE_string('gcs_prefix', 'gs://gresearch/deep-ope/d4rl',
                    'GCS prefix for policy snapshots.')
flags.DEFINE_string('policies_json', 'd4rl_policies.json',
                    'Path to policies json.')
FLAGS = flags.FLAGS


class Policy:
  """D4RL policy."""

  def __init__(self, policy_file):
    with tf.io.gfile.GFile(os.path.join(FLAGS.gcs_prefix, policy_file),
                           'rb') as f:
      weights = pickle.load(f)
    self.fc0_w = weights['fc0/weight']
    self.fc0_b = weights['fc0/bias']
    self.fc1_w = weights['fc1/weight']
    self.fc1_b = weights['fc1/bias']
    self.fclast_w = weights['last_fc/weight']
    self.fclast_b = weights['last_fc/bias']
    self.fclast_w_logstd = weights['last_fc_log_std/weight']
    self.fclast_b_logstd = weights['last_fc_log_std/bias']
    relu = lambda x: np.maximum(x, 0)
    self.nonlinearity = np.tanh if weights['nonlinearity'] == 'tanh' else relu

    identity = lambda x: x
    self.output_transformation = np.tanh if weights[
        'output_distribution'] == 'tanh_gaussian' else identity

  def act(self, state, noise):
    x = np.dot(self.fc0_w, state) + self.fc0_b
    x = self.nonlinearity(x)
    x = np.dot(self.fc1_w, x) + self.fc1_b
    x = self.nonlinearity(x)
    mean = np.dot(self.fclast_w, x) + self.fclast_b
    logstd = np.dot(self.fclast_w_logstd, x) + self.fclast_b_logstd

    action = self.output_transformation(mean + np.exp(logstd) * noise)
    return action, mean


def main(_):
  with tf.io.gfile.GFile(FLAGS.policies_json, 'r') as f:
    policy_database = json.load(f)

  # Choose a policy
  policy_metadata = policy_database[42]
  pprint.pprint(policy_metadata)

  env_name = policy_metadata['task.task_names'][0]
  env = gym.make(env_name)

  policy = Policy(policy_metadata['policy_path'])

  # Evaluate random rollouts.
  all_returns = []
  for _ in range(10):
    s = env.reset()
    returns = 0
    gamma = 1.0
    for t in range(env._max_episode_steps):  # pylint:disable=protected-access
      noise_input = np.random.randn(env.action_space.shape[0]).astype(
          np.float32)
      action, _ = policy.act(s, noise_input)
      s, r, d, _ = env.step(action)
      returns += (gamma**t) * r
      if d:
        break
    print(returns, end='\r')
    all_returns.append(returns)

  print(env_name, ':', np.mean(all_returns))


if __name__ == '__main__':
  app.run(main)
