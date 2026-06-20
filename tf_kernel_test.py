# -*- coding: utf-8 -*-
#   Project: CISE-QE-DBA File: tf_kernel_test.py  Created: 6/19/26 23:15 Author: etyrer & his robot dog™


from nbformat.v4 import new_notebook, new_code_cell
from nbclient import NotebookClient

nb = new_notebook(
    cells=[
        new_code_cell(
            "from tensorflow.keras.utils import save_img\nprint('SUCCESS')"
        )
    ]
)

client = NotebookClient(nb, timeout=600)

with client.setup_kernel():
    client.execute()

print("DONE")