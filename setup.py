from setuptools import setup, find_packages

packages = find_packages()

setup(name='dockerspawner_usermap',
      version='0.1',
      description='Maps docker nbserver containers to '
                  'unix users directories. Such that users'
                  'accounts and their home directories can'
                  'be mapped into the container',
      url='http://github.com/kayibal/dockerspawner_usermap',
      author='Alan Höng',
      author_email='alan.f.hoeng@gmail.com',
      install_requires=["dockerspwaner"],
      packages=packages,
      zip_safe=False)
