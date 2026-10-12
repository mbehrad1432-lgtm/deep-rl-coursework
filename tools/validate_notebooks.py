"""Schema and IPython syntax validation; never executes notebook source."""
from pathlib import Path
import json,warnings,ast
import nbformat
from IPython.core.inputtransformer2 import TransformerManager
root=Path(__file__).resolve().parents[1];transformer=TransformerManager();results=[]
for path in sorted(root.glob('*/*.ipynb')):
    notebook=nbformat.read(path,as_version=4)
    nbformat.validate(notebook)
    syntax=[]
    for index,cell in enumerate(notebook.cells):
        if cell.cell_type != 'code' or not cell.source.strip():continue
        try:ast.parse(transformer.transform_cell(cell.source))
        except SyntaxError as error:syntax.append({'cell':index,'message':error.msg})
    results.append({'notebook':str(path.relative_to(root)),'schema':'valid','syntax_errors':syntax})
report={'mode':'schema and syntax only; no cells executed','notebooks_checked':len(results),'results':results}
(root/'STATIC_REVIEW.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
if any(row['syntax_errors'] for row in results):raise SystemExit(1)
