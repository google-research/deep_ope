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

set -e
set -x

virtualenv -p python3 .
source ./bin/activate

pip install -r requirements.txt

if [[ ! -d deepmind-research ]]; then
  git clone --depth 1 --filter=blob:none --sparse https://github.com/deepmind/deepmind-research.git;
  cd deepmind-research
  git sparse-checkout init --cone
  git sparse-checkout set rl_unplugged
  cd ..
fi
PYTHONPATH=$PYTHONPATH:`pwd`/deepmind-research/rl_unplugged

python load_rlunplugged_policy_example.py
python load_d4rl_policy_example.py
