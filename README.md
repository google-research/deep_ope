<img src="./images/tasks.png" width="50%">

# [Benchmarks for Deep Off-Policy Evaluation](https://openreview.net/forum?id=kWSeGEeHvF8)
### Contact: offline-rl@google.com

In
[D4RL](https://sites.google.com/view/d4rl/home) and [RL Unplugged: Benchmarks for Offline Reinforcement Learning](https://arxiv.org/abs/2006.13888),
we released a suite of benchmarks for offline reinforcement learning. They are designed to facilitate ease of use, so we provided the datasets
with a unified API which makes it easy for the practitioner to work with all
data in the suite once a general pipeline has been established.

Here, we release policies which can be used in conjunction with the RL Unplugged
and D4RL datasets to facilitate off-policy evaluation and offline model selection
benchmarking.

In this release, we provide:

-   Policies for the tasks in the D4RL, DeepMind Locomotion and Control Suite datasets
    (described below).

-   Policies trained with the following algorithms (D4PG, ABM, CRR, SAC, DAPG and BC) and snapshots along the training trajectory. This faciliates benchmarking offline model selection.

The policies are available under
[gs://gresearch/deep-ope](https://console.cloud.google.com/storage/browser/gresearch/deep-ope), with the RL Unplugged policies in the subdirectory [gs://gresearch/deep-ope/rlunplugged](https://console.cloud.google.com/storage/browser/gresearch/deep-ope/rlunplugged) and the D4RL policies in the subdirectory [gs://gresearch/deep-ope/d4rl](https://console.cloud.google.com/storage/browser/gresearch/deep-ope/d4rl).

## Task Descriptions

### DeepMind Locomotion Dataset

These tasks are made up of the corridor locomotion tasks involving the CMU
Humanoid, for which prior efforts have either used motion capture data
([Merel et al., 2019a], [Merel et al., 2019b]) or training from scratch
([Song et al., 2020]). In addition, the DM Locomotion repository contains a set of
tasks adapted to be suited to a virtual rodent ([Merel et al., 2020]). We
emphasize that the DM Locomotion tasks feature the combination of challenging
high-DoF continuous control along with perception from rich egocentric
observations. For details on how the dataset was generated, please refer to
[RL Unplugged: Benchmarks for Offline Reinforcement Learning](https://arxiv.org/abs/2006.13888).

### DeepMind Control Suite Dataset

DeepMind Control Suite ([Tassa et al., 2018]) is a set of control tasks
implemented in MuJoCo ([Todorov et al., 2012]). We consider a subset of the tasks
provided in the suite that cover a wide range of difficulties.

Most of the datasets in this domain are generated using D4PG. For the
environments Manipulator insert ball and Manipulator insert peg we use V-MPO
([Song et al., 2020]) to generate the data as D4PG is unable to solve these tasks.
We release datasets for 9 control suite tasks. For details on how the dataset
was generated, please refer to
[RL Unplugged: Benchmarks for Offline Reinforcement Learning](https://arxiv.org/abs/2006.13888).

### D4RL Dataset

A subset of the tasks within the D4RL ([Fu et. al. 2020]) for offline reinforcement
learning is included. These tasks include maze navigation with different robot
morphologies, hand manipulation tasks ([Rajeswaran et. al. 2017]), and tasks from
the OpenAI Gym bechmark ([Brockman et. al. 2016]).

Each task includes a variety of datasets in order to study the interaction between
dataset distributions and policies. For further information on what datasets
are available, please refer to [D4RL: Datasets for Deep Data-Driven Reinforcement Learning](https://arxiv.org/abs/2004.07219).

## Using the policies

The `rlunplugged_policies.json` file provides metadata about the policies in this dataset.
It is structured as a list of dictionaries, one for each policy, where the keys
contain metadata including:

-   policy_path: The path to the policy on Google Cloud Storage.

-   task.task_name: The task that the policy is trained for.

-   agent_name: The training algorithm used to learn the policy.

-   snapshot_name: Contains the learning step for this policy snapshot.

-   return_mean: The mean return estimated with Monte Carlo rollouts.

-   return_std: The standard error of the mean estimate.

The 'd4rl_policies.json' file contains metadata in a similar format:

-   policy_path: The path to the policy on Google Cloud Storage.

-   task.task_names: A list of tasks that the policy is trained for. (Each task represets a different dataset)

-   agent_name: The training algorithm used to learn the policy.

-   return_mean: The mean return estimated with Monte Carlo rollouts.

-   return_std: The standard error of the mean estimate.

Requirements:

*   Install dependencies: `pip install -r requirements.txt`
*   (Optional) Setup MuJoCo license key for DM Control and D4RL environments
    ([instructions](https://github.com/deepmind/dm_control#requirements-and-installation)).

### Policy loading example

RLUnplugged policies are stored as
[TensorFlow SavedModels](https://www.tensorflow.org/guide/saved_model). Calling
the policy on an observation returns an action sample. See `load_rlunplugged_policy_example.py` for an example of loading a policy.

D4RL policies are stored as pickle files containing weights.
See `load_d4rl_policy_example.py` for an example of loading a policy.
### Compute evaluation metrics

```
TODO Fill in example computing groundtruth and evaluation metrics.
```

## Dataset Metadata

The following table is necessary for this dataset to be indexed by search
engines such as <a href="https://g.co/datasetsearch">Google Dataset Search</a>.
<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td><code itemprop="name">Benchmarks for Deep Off-Policy Evaluation</code></td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/google-research/deep_ope</code></td>
  </tr>
  <tr>
    <td>sameAs</td>
    <td><code itemprop="sameAs">https://github.com/google-research/deep_ope</code></td>
  </tr>
  <tr>
    <td>description</td>
    <td><code itemprop="description">
      Data accompanying
[Benchmarks for Deep Off-Policy Evaluation]().
      </code></td>
  </tr>
  <tr>
    <td>provider</td>
    <td>
      <div itemscope itemtype="http://schema.org/Organization" itemprop="provider">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">Google</code></td>
          </tr>
          <tr>
            <td>sameAs</td>
            <td><code itemprop="sameAs">https://en.wikipedia.org/wiki/Google</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
</table>
</div>

[Agarwal et al., 2020]: https://arxiv.org/abs/1907.04543
[Brockman et. al. 2016]: https://arxiv.org/abs/1606.01540
[Fu et. al. 2020]: https://arxiv.org/abs/2004.07219
[Machado et al., 2018]: https://arxiv.org/abs/1709.06009
[Merel et al., 2019a]: https://arxiv.org/abs/1811.09656
[Merel et al., 2019b]: https://arxiv.org/abs/1811.11711
[Merel et al., 2020]: https://arxiv.org/abs/1911.09451
[Rajeswaran et. al. 2017]: https://arxiv.org/abs/1709.10087
[Song et al., 2020]: https://arxiv.org/abs/1909.12238
[Tassa et al., 2018]: https://arxiv.org/abs/1801.00690
[Todorov et al., 2012]: https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf
