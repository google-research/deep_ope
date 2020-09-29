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
import pprint

from absl import app
from absl import flags
from dm_control_suite import ControlSuite
import tensorflow as tf
import tree

flags.DEFINE_string('gcs_prefix', 'gs://offline-rl/evaluation',
                    'GCS prefix for policy snapshots.')
flags.DEFINE_string('policies_json', 'policies.json', 'Path to policies json.')
FLAGS = flags.FLAGS


def main(_):
  with tf.io.gfile.GFile(FLAGS.policies_json, 'r') as f:
    policy_database = json.load(f)

  # Choose a policy
  policy_metadata = policy_database[42]
  pprint.pprint(policy_metadata)

  # Load policy snapshot from GCS
  policy = tf.saved_model.load(os.path.join(FLAGS.gcs_prefix,
                                            policy_metadata['policy_path']))

  task = ControlSuite(
      task_name=policy_metadata['task.task_name'])
  environment = task.environment
  timestep = environment.reset()
  observation = timestep.observation
  print('Observation:')
  pprint.pprint(observation)

  # Add batch dimension to observation
  batched_observation = tree.map_structure(lambda x: x[None, :], observation)
  # All policies are non-recurrent, however, some policies were saved with the
  # recurrent API, so they must be called with an initial_state.
  # TODO(gjt): Resave policies in non-recurrent API.
  if hasattr(policy, 'initial_state'):
    action = policy(batched_observation, ((),))[0]
  else:
    action = policy(batched_observation)
  print('Action:')
  pprint.pprint(action)

if __name__ == '__main__':
  app.run(main)
