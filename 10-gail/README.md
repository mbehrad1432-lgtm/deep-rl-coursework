# GAIL with PPO and Reward Ablations

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

Historical evaluation reports expert 499.6 and default GAIL 500, while alternative reward labels airl and logd report 9.3. The airl option is a log-odds reward variant, not a complete AIRL architecture. Demo-count comparisons are single-run observations; more demonstrations did not monotonically improve saved outcomes.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
