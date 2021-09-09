import shutil
from os.path import exists


class PyVersion:
    
    def __init__(self, version: str):
        self._version = version
        a, b, c, *_ = (version + '.0.0.0').split('.')
        self.major = int(a)
        self.minor = int(b)
        self.patch = int(c)
    
    def __str__(self):
        return self._version
    
    @property
    def v(self):
        """
        Returns:
            self._version = 'python39' -> 'python39'
            self._version = 'python39-32' -> 'python39-32'
        """
        return self._version
    
    @property
    def v0(self):
        """
        Returns:
            self._version = 'python39' -> 'python39'
            self._version = 'python39-32' -> 'python39'
        """
        if '-' in self._version:
            return self._version.split('-')[0]
        else:
            return self._version
    
    @property
    def v1(self):
        """
        Returns:
            self._version = 'python39' -> '39'
            self._version = 'python39-32' -> '39-32'
        """
        return self._version.removeprefix('python')


class EmbedPythonManager:
    
    def __init__(self, pyversion: PyVersion):
        from .path_model import AssetsPathModel
        self.pyversion = pyversion
        self.model = AssetsPathModel(pyversion)
        self.model.build_dirs()
        
        self.python = f'{self.model.pyversion}/python.exe'
        self.pythonw = f'{self.model.pyversion}/pythonw.exe'
    
    def download(self):
        from .downloader import EmbedPythonDownloader
        dl = EmbedPythonDownloader()
        dl.main(self.pyversion)
        del EmbedPythonManager, dl
    
    def copy_to(self, dst_dir):
        shutil.copytree(self.model.pyversion, dst_dir)
    
    # --------------------------------------------------------------------------
    # status
    
    @property
    def is_pth_disabled(self):
        return not exists(self.model.python_pth)
    
    @property
    def has_pip(self):
        return exists(self.model.pip)
    
    @property
    def has_setuptools(self):
        return exists(self.model.setuptools)
    
    @property
    def has_pip_script(self):
        return exists(self.model.pip_script)
