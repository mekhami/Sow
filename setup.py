#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='harvest-sow',
      packages = find_packages(),
      version='1.0.0b1',
      description='Harvest Command Line App',
      author='Lawrence Vanderpool',
      author_email='lawrence.vanderpool@gmail.com',
      url='http://www.github.com/mekhami/Sow',
      install_requires=['docopt', 'keyring', 'python-harvest'],
      license='MIT',
      keywords='harvest sow api',
      entry_points={
          'console_scripts': [
              'sow = sow.console:main'
            ]
        }
      )
