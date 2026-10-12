# RL2, MAML and VariBAD-Style Meta-RL

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

Separate synthetic plotting demonstrations (source cells 51 and 52) from real training outputs. The five-seed actual first-rollout → adapted mean returns are VariBAD −218.996 → −219.368, MAML −244.290 → −244.680, RL2 −270.850 → −271.555; these show no positive mean adaptation gain. One-million-frame settings and sparse evaluation are not the full paper budget or a faithful paper reproduction. VariBAD-style is an educational variant.

## Attribution

Original course, template and reference credits remain in the notebook. Completed assignment templates do not establish sole authorship. Confirm personal contributions before using the CV wording. No new license is assigned to course material or third-party assets. Student number and transient metadata were removed.
