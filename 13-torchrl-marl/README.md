# MADDPG and MAPPO with TorchRL and VMAS

Coursework portfolio notebook for Behrad Mazaheri.

## Contents

- `notebook.ipynb`: supplied implementation with historical outputs, review banner and privacy cleanup.
- `REVIEW.md`: interpretation limits and implementation concerns.
- `DATA_REQUIREMENTS.md`: runtime inputs and missing files.
- `requirements.txt`: dependency inventory, not a tested lockfile.
- `evidence/`: source hash, execution inventory and saved text outputs.

## Use

Read the review and input requirements first. Create a separate environment for this folder, install dependencies, launch Jupyter, and open the notebook. Run from this folder unless source paths specify otherwise. Historical outputs may depend on old APIs, seeds, hardware or files absent here. No training or Run-All was performed during packaging.

## Result interpretation

Uses TorchRL loss/collector implementations rather than implementing every algorithm from scratch. DDPG budget is 500 × 6000 = 3,000,000 frames; PPO budget is 20 × 6000 = 120,000 frames. Curves therefore do not establish a fair algorithm ranking. TorchRL/TensorDict/VMAS API versions matter; dependency names below are not a compatibility-tested lockfile.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
