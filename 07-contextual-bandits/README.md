# Contextual Bandits and Moderation Simulation

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

Text examples are real, but action rewards, logged propensities and cost profiles are simulated. Severity is a proxy derived from binary labels. NeuralUCB-style uses LinUCB on frozen learned features. OPE uses the same log for fitting and estimation without cross-fitting; it is not unbiased evidence for a deployed policy. Safety masks are experimental heuristics, not a production safety guarantee.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
