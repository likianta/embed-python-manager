# Install

```
git clone https://github.com/Likianta/embed-python-manager.git
```

# How To Use

Open this project in PyCharm, create a test script and copy the following code to test:

```python
# ~/embed-python-manager/test.py
# Notice: this is basic usage of embed_python_manager. Advanced usage is not 
#   ready to provide.
 
from embed_python_manager import EmbedPythonManager

manager = EmbedPythonManager('python39')

# Internet connection required.
manager.deploy(add_pip_suits=True, add_tk_suits=False)
#   Now the embedded Python folder is ready to call, copy, move and more.

manager.copy_to(input('Target venv folder: '))
# manager.move_to(input('Target venv folder: '))

```
