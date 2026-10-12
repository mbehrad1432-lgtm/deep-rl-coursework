# Deep Reinforcement Learning Coursework

Portfolio packaging for **Behrad Mazaheri**: 14 supplied notebooks covering value-based RL, policy gradients, continuous control, planning, exploration, offline RL, imitation, multi-agent learning and meta-RL. Some assignments are tabular or linear-policy foundations rather than deep RL. Original course/template credits remain; personal contribution boundaries require confirmation.

**Review mode: source and saved-output inspection only. No notebook execution, environment rollout, retraining or paper-result reproduction.**

## Projects

| Folder | Topic |
|---|---|
| [01-half-rainbow-dqn](01-half-rainbow-dqn/README.md) | DQN, Double DQN, Dueling and Prioritized Replay |
| [02-natural-policy-gradient](02-natural-policy-gradient/README.md) | Natural Policy Gradient on MiniTetris |
| [03-reinforce](03-reinforce/README.md) | REINFORCE and Baselines |
| [04-dpg-ddpg-td3](04-dpg-ddpg-td3/README.md) | DPG, DDPG and TD3 on Moving Reacher |
| [05-dyna-q](05-dyna-q/README.md) | Dyna-Q, Reward Shaping and Prioritized Sweeping |
| [06-muzero-style-search](06-muzero-style-search/README.md) | MuZero-Style Models and Monte Carlo Tree Search |
| [07-contextual-bandits](07-contextual-bandits/README.md) | Contextual Bandits and Moderation Simulation |
| [08-deepsea-exploration](08-deepsea-exploration/README.md) | DeepSea Exploration with RND and Bootstrap Ensembles |
| [09-offline-ddpg-bc](09-offline-ddpg-bc/README.md) | Offline DDPG and Behavior Cloning |
| [10-gail](10-gail/README.md) | GAIL with PPO and Reward Ablations |
| [11-minigrid-imitation](11-minigrid-imitation/README.md) | Behavior Cloning and DAgger on MiniGrid |
| [12-matrix-games](12-matrix-games/README.md) | Fictitious Play and Regret in Matrix Games |
| [13-torchrl-marl](13-torchrl-marl/README.md) | MADDPG and MAPPO with TorchRL and VMAS |
| [14-meta-rl](14-meta-rl/README.md) | RL2, MAML and VariBAD-Style Meta-RL |

## Evidence and limitations

Each project retains historical notebook outputs and supplies a dependency inventory, input requirements, review and text-output evidence. `inventory.json` records original source hashes and execution counts; `STATIC_REVIEW.json` records schema/syntax checks only. Embedded figures remain historical. Missing Moving Reacher and DeepSea course modules block their fresh execution. Bandit action rewards are simulated. Meta-RL includes explicitly synthetic plotting demos separate from real training. MADDPG and MAPPO use unequal frame budgets. See project reviews before citing scores.

One DQN copy changes time-limit target masking and has every output cleared. Extracted DeepSea student modules come from embedded writefile cells and are not a replacement framework.

## GitHub preparation

Create a separate `deep-rl-coursework` repository. Extract the ZIP and upload its contents, including this README; do not upload the ZIP itself. Include attribution and reviews. Dependency inventories are intentionally unpinned because package compatibility was not tested. Avoid adding generated datasets, weights, secrets and transient outputs.

## Static verification

Install `nbformat` and `ipython`, then run `python tools/validate_notebooks.py`. This checks notebook schema and transformed Python syntax, never runs cells. It does not verify numerical correctness, runtime dependencies or training results.
