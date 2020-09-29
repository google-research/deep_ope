<img src="./images/tasks.png" width="50%">

# Benchmarks for Deep Off-Policy Evaluation
### Contact: offline-rl@google.com

In
[D4RL](https://sites.google.com/view/d4rl/home) and [RL Unplugged: Benchmarks for Offline Reinforcement Learning]([https://arxiv.org/abs/2006.13888]),
we released a suite of benchmarks for offline reinforcement learning. They are designed to facilitate ease of use, so we provided the datasets
with a unified API which makes it easy for the practitioner to work with all
data in the suite once a general pipeline has been established.

Here, we release policies which can be used in conjunction with the RL Unplugged
datasets to facilitate off-policy evaluation and offline model selection
benchmarking. Policies for the D4RL dataset can be found [here](https://sites.google.com/view/d4rl/home).

In this release, we provide:

-   Policies for the tasks in the DeepMind Locomotion and Control Suite datasets
    (described below).

-   Policies trained with the following algorithms (D4PG, ABM, CRR and BC) and snapshots along the training trajectory. This faciliates benchmarking offline model selection.
<!-- TODO(gjt): Discuss D4RL policies and add an API to show how to load the D4RL policies into TF. -->

The policies are available under
[gs://offline-rl/evaluation](gs://offline-rl/evaluation).

## Task Descriptions

### DeepMind Locomotion Dataset

These tasks are made up of the corridor locomotion tasks involving the CMU
Humanoid, for which prior efforts have either used motion capture data
[Merel et al., 2019a], [Merel et al., 2019b] or training from scratch
[Song et al., 2020]. In addition, the DM Locomotion repository contains a set of
tasks adapted to be suited to a virtual rodent [Merel et al., 2020]. We
emphasize that the DM Locomotion tasks feature the combination of challenging
high-DoF continuous control along with perception from rich egocentric
observations. For details on how the dataset was generated, please refer to
[RL Unplugged: Benchmarks for Offline Reinforcement Learning]([https://arxiv.org/abs/2006.13888]).

### DeepMind Control Suite Dataset

DeepMind Control Suite [Tassa et al., 2018] is a set of control tasks
implemented in MuJoCo [Todorov et al., 2012]. We consider a subset of the tasks
provided in the suite that cover a wide range of difficulties.

Most of the datasets in this domain are generated using D4PG. For the
environments Manipulator insert ball and Manipulator insert peg we use V-MPO
[Song et al., 2020] to generate the data as D4PG is unable to solve these tasks.
We release datasets for 9 control suite tasks. For details on how the dataset
was generated, please refer to
[RL Unplugged: Benchmarks for Offline Reinforcement Learning]([https://arxiv.org/abs/2006.13888]).

## Using the policies

The `policies.json` file provides metadata about the policies in this dataset.
It is structured as a list of dictionaries, one for each policy, where the keys
contain metadata including:

-   policy_path: The path to the policy on Google Cloud Storage.

-   task.task_name: The task that the policy is trained for.

-   agent_name: The training algorithm used to learn the policy.

-   snapshot_name: Contains the learning step for this policy snapshot.

-   return_mean: The mean return estimated with Monte Carlo rollouts.

-   return_sem: The standard error of the mean estimate.

Requirements:

*   Install dependencies: `pip install -r requirements.txt`
*   (Optional) Setup MuJoCo license key for DM Control environments
    ([instructions](https://github.com/deepmind/dm_control#requirements-and-installation)).

### Policy loading example

Policies are stored as
[TensorFlow SavedModels](https://www.tensorflow.org/guide/saved_model). Calling
the policy on an observation returns an action sample. See `load_policy_example.py` for an example of loading a policy.

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
[Machado et al., 2018]: https://arxiv.org/abs/1709.06009
[Merel et al., 2019a]: https://arxiv.org/abs/1811.09656
[Merel et al., 2019b]: https://arxiv.org/abs/1811.11711
[Merel et al., 2020]: https://arxiv.org/abs/1911.09451
[Song et al., 2020]: https://arxiv.org/abs/1909.12238
[Tassa et al., 2018]: https://arxiv.org/abs/1801.00690
[Todorov et al., 2012]: https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf
