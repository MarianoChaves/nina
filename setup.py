from setuptools import setup, find_packages

setup(
   name='NInA',
   version='0.0',
   description='Neutrino interface application',
   author='Mariano Chaves',
   author_email='mchaves@unicamp.com.br',
   packages=find_packages(exclude=["docs","tests", ".gitignore", "README.rst","DESCRIPTION.rst"]),
   install_requires=['numpy'], #external packages as dependencies
   package_dir={'':'src'}
)