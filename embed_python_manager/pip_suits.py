"""
If you want only pip package installed, run `get_pip` and it is fast to
generate.
If you need '~/scripts/pip.exe' etc., run `get_pip_scripts`. Note that `get_pip_
scripts` can only generate pip scripts, no package being installed; you may
need also to run `get_pip` after that.

References:
    ~/docs/depsland-venv-setup.md
"""
from os.path import exists
from shutil import rmtree

from lk_utils import run_cmd_args


from .path_model import assets_model
from .manager import PyVersion
from .downloader import download, extract


def download_setuptools(pyversion: PyVersion):
    if pyversion.major == 2:
        # name = 'setuptools-45.0.0-py2.py3-none-any.whl'
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/af/e7/02db816dc88c' \
               '598281bacebbb7ccf2c9f1a6164942e88f1a0fded8643659/setuptools-4' \
               '5.0.0-py2.py3-none-any.whl#sha256=001c474c175697a03e2afffd87d' \
               '92411c89215be5f2cd3e0ab80a67726c0f4c2'
    elif pyversion.major == 3:
        # name = 'setuptools-58.0.4-py3-none-any.whl'  # 2021-09-09
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/c4/c1/aed7dfedb18e' \
               'a73d7713bf6ca034ab001a6425be49ffa7e79bbd5999f677/setuptools-5' \
               '8.0.4-py3-none-any.whl#sha256=69cc739bc2662098a68a9bc575cd974' \
               'a57969e70c1d58ade89d104ab73d79770'
    else:
        raise Exception(pyversion)
    
    file = download(link, assets_model.setuptools_in_pip_suits + '.whl')
    extract(file, assets_model.setuptools_in_pip_suits)
    
    
def download_pip_src(pyversion: PyVersion):
    if pyversion.major == 2:
        # name = 'pip-20.3.4.tar.gz'
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/53/7f/55721ad0501a' \
               '9076dbc354cc8c63ffc2d6f1ef360f49ad0fbcce19d68538/pip-20.3.4.t' \
               'ar.gz#sha256=6773934e5f5fc3eaa8c5a44949b5b924fc122daa0a8aa9f8' \
               '0c835b4ca2a543fc'
    elif pyversion.major == 3:
        # name = 'pip-21.2.4.tar.gz'  # 2021-09-09
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/52/e1/06c018197d81' \
               '51383f66ebf6979d951995cf495629fc54149491f5d157d0/pip-21.2.4.t' \
               'ar.gz#sha256=0eb8a1516c3d138ae8689c0c1a60fde7143310832f9dc77e' \
               '11d8a4bc62de193b'
    else:
        raise Exception(pyversion)
    
    file = download(link, assets_model.pip_src_in_pip_suits + '.tar.gz')
    extract(file, assets_model.pip_src_in_pip_suits, type_='tar')
    
    
def download_pip(pyversion: PyVersion):
    if pyversion.major == 2:
        # name = 'pip-20.3.4-py2.py3-none-any.whl'
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/27/79/8a850fe34964' \
               '46ff0d584327ae44e7500daf6764ca1a382d2d02789accf7/pip-20.3.4-p' \
               'y2.py3-none-any.whl#sha256=217ae5161a0e08c0fb873858806e3478c9' \
               '775caffce5168b50ec885e358c199d'
    elif pyversion.major == 3:
        # name = 'pip-21.2.4-py3-none-any.whl'  # 2021-09-09
        link = 'https://pypi.tuna.tsinghua.edu.cn/packages/ca/31/b88ef447d595' \
               '963c01060998cb329251648acf4a067721b0452c45527eb8/pip-21.2.4-p' \
               'y3-none-any.whl#sha256=fa9ebb85d3fd607617c0c44aca302b1b45d87f' \
               '9c2a1649b46c26167ca4296323'
    else:
        raise Exception(pyversion)
    
    file = download(link, assets_model.pip_in_pip_suits + '.whl')
    extract(file, assets_model.pip_in_pip_suits)


def get_setuptools():
    pass
    
    
def get_pip_scripts(dst_dir):
    mklinks(assets_struct.setuptools, dst_dir)
    
    run_cmd_args('cd', '')
    send_cmd('cd {pip_src_dir} & {python} setup.py install'.format(
        pip_src_dir=assets_struct.pip_src,
        python=src_struct.interpreter,
        pip_src=assets_struct.pip_src,
    ).replace('/', '\\'))
    
    assert exists(f'{src_struct.scripts}/pip.exe')
    
    rmtree(src_struct.site_packages + '/' + assets_struct.pip_egg)


def get_pip(dst_dir):
    out = []
    out.extend(mklinks(assets_struct.setuptools, dst_dir, exist_ok=True))
    out.extend(mklinks(assets_struct.pip, dst_dir, exist_ok=False))
    return out
