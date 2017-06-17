from distutils.core import setup, Extension

tribus_hash_module = Extension('tribus_hash',
                               sources = ['tribusmodule.c',
                                          'tribus.c',
										  'sph/aes_helper.c',
										  'sph/sph_jh.c',
										  'sph/sph_keccak.c',
										  'sph/sph_echo.c'],
                               include_dirs=['.', './sph'])

setup (name = 'tribus_hash',
       version = '1.0',
       description = 'Bindings for tribus proof of work used by Denarius',
       ext_modules = [tribus_hash_module])
