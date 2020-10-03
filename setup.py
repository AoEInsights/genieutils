#!/usr/bin/env python
import os
from distutils.core import setup, Extension

from setuptools import find_packages


dat_file = Extension('GenieUtils._DatFile',
                     libraries=['genieutils'],
                     include_dirs=['GenieUtils/var/genieutils/include'],
                     library_dirs=['GenieUtils/var/build/'],
                     runtime_library_dirs=['$ORIGIN/var/build/'],
                     sources=['GenieUtils/DatFile_wrap.cxx'])

setup(name='GenieUtils',
      version='1.0',
      author='Kevin Armenat',
      author_email='kevin@armen.at',
      packages=find_packages(),
      ext_modules=[dat_file],
      include_package_data=True)
