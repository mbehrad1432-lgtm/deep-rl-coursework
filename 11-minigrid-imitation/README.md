# Behavior Cloning and DAgger on MiniGrid

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

BFS expert has privileged symbolic environment access; the learner uses observations. A transition-level split can share trajectories between train and validation. Saved success: BC 50%, best selected DAgger 77.5%, best selected critical-state variant 65%. Selecting the best iteration on the same evaluation episodes is optimistic; use separate validation and final test seeds for a new experiment. Success is not monotonic across iterations or label budgets.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
