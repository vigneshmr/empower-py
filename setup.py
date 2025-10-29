from distutils.core import setup
version = '1.0.1'

setup(
  name = 'empower-py',  # PyPI package name can have hyphens
  packages = ['empower_py'],  # Python module name must use underscores
  version = version,
  description = 'Library for accessing Empower personal dashboard API',
  author = 'Vignesh',
  url = 'https://github.com/vigneshmr/empower-py',
  download_url = '://github.com/vigneshmr/empower-py/tarball/{0}'.format(version),
  keywords = ['empower', 'financial', 'money'],
  classifiers = [],
)
