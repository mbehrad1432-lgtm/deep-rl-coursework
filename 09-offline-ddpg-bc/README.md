# Offline DDPG and Behavior Cloning

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

Normalization and Q-scaled behavior-cloning regularization are studied on generated offline data. Replay stores true termination separately from time limits. The narrow alpha sweep has similar poor returns; do not claim optimal alpha or broad offline-RL superiority. An unexecuted bonus definition is not an evaluated result.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
