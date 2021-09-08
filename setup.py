# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('main.py',
                          targetName='KompasMass.exe',
                          base='Win32GUI',
                          icon='images/icon.ico')
              ]

excludes = ['unittest', 'email', 'html', 'http', 'xml',
            'unicodedata', 'bz2', 'select', 'PyQt5']

include_files = ['config.ini', 'images']

zip_include_packages = ['collections', 'encodings', 'importlib']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='KompasMass',
      version='1.0',
      description='Kompas app',
      executables=executables,
      options=options)