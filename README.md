# Install

```
pip install embed-python-manager
```

# Basic Usages

```python
from embed_python_manager import EmbedPythonManager

manager = EmbedPythonManager('python39')

# Internet connection required.
manager.deploy(add_pip_suits=True, add_tk_suits=False)
#   Now the embedded Python folder is ready to call, copy, move and more.

manager.copy_to(input('Target venv folder: '))
# manager.move_to(input('Target venv folder: '))

```

# Advanced Usages

*TODO*
