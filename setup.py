#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Sow',
      packages = find_packages(),
      version='0.1',
      description='Harvest Command Line App',
      author='Lawrence Vanderpool',
      author_email='lawrence.vanderpool@gmail.com',
      url='http://www.github.com/mekhami/Sow',
      install_requires=['docopt', 'keyring'],
      entry_points={
          'console_scripts': [
              'sow = sow.console:main'
            ]
        }
      )
