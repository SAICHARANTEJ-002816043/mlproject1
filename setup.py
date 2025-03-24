from setuptools import find_packages,setup

setup(
  name = 'mlproject',
  version='0.0.1',
  author = 'charan',
  author_email= 'katteboina.s@northeastern.edu',
  packages = find_packages(),
  install_requires = ['pandas','numpy','seaborn']
  
)