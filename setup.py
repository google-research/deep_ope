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

from setuptools import find_packages
from setuptools import setup

setup(
    name='deep_ope',
    description=(
        'Deep OPE: Benchmarks for Off-policy Evaluation and Offline Policy Selection'
    ),
    author='Google LLC',
    author_email='no-reply@google.com',
    url='https://github.com/google-research/deep_ope',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={},
    install_requires=[
        'absl-py==0.10.0',
        'dm-acme==0.1.8',
        'dm-control==0.0.322773188',
        'dm-env==1.2',
        'dm-reverb==0.1.0',
        'dm-tree==0.1.5',
        'gym==0.17.2',
        'tensorflow==2.3.0',
    ])
