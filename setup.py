#!/usr/bin/env python

from distutils.core import setup, Extension

dat_file = Extension('_DatFile',
                     libraries=['genieutils'],
                     include_dirs=['var/genieutils/include'],
                     library_dirs=['var/build/'],
                     runtime_library_dirs=['var/build/'],
                     sources=['DatFile_wrap.cxx'])

setup(name='GenieUtils',
      version='1.0',
      author='Kevin Armenat',
      author_email='kevin@armen.at',
      ext_modules=[dat_file])
