#!/bin/bash
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

# Download D4RL policies.
# NOTE: If this fails, you may need to log in with `gcloud auth login'.
pip install gsutil
gsutil -m cp -r gs://gresearch/deep-ope/d4rl /tmp

# Download policy eval code.
git clone --depth 1 --filter=blob:none --sparse https://github.com/google-research/google-research.git;
cd google-research
git sparse-checkout init --cone
git sparse-checkout set policy_eval

set -e
set -x

virtualenv -p python3 .
source ./bin/activate

# The below command requires proper installation of mujoco-py. See
# https://github.com/openai/mujoco-py#install-mujoco
pip install -r policy_eval/requirements.txt

# By default, the below command will take a long time to run. To shorten it,
# simply pass in smaller numbers for num_mc_episodes and num_updates.
python -m policy_eval.train_eval --logtostderr --d4rl \
  --env_name=halfcheetah-medium-v0 \
  --d4rl_policy_filename=/tmp/d4rl/halfcheetah/halfcheetah_online_0.pkl \
  --target_policy_std=0.0 --num_mc_episodes=256 --nobootstrap --algo=fqe \
  --noise_scale=0.0 --num_updates=1000000
