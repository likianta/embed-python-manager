# Add New Python Interpreter

For example adding python 3.10.0:

- Update all yaml files under `embed_python_manager/source_list`.
    - TODO: for now there's no automation tool to update all of them.

# Upgrade `pip` Suits

Open `embed_python_manager/pip_suits.py`...

- Check and update all comment blocks.
- Refresh download links in functions whose name starts with `download_`

# Other

[Depsland project](https://github.com/likianta/depsland) has pre-downloaded some
resources in its "build" folder. We need to update them too.

See also `depsland/build/assets/post_build`.
