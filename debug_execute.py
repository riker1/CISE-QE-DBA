import nbformat
from nbclient import NotebookClient

nb = nbformat.read("Demo.ipynb", as_version=4)

client = NotebookClient(
    nb,
    timeout=-1,
    iopub_timeout=300,
    kernel_name="python3",
)

debug_cell = nbformat.v4.new_code_cell("""
import faulthandler, sys
faulthandler.enable()
faulthandler.dump_traceback_later(60, repeat=True, file=sys.__stderr__)
print("faulthandler enabled")
""")

with client.setup_kernel():
    print("--- Running debug setup cell ---", flush=True)
    client.execute_cell(debug_cell, -1)

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue

        print(f"\\n--- Running cell {i} ---", flush=True)
        print(cell.source[:500], flush=True)

        client.execute_cell(cell, i)

        print(f"--- Finished cell {i} ---", flush=True)

nbformat.write(nb, "Demo.executed.ipynb")
print("Wrote Demo.executed.ipynb", flush=True)