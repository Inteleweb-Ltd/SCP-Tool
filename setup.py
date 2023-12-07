from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', icon="src/iweb_icon.ico" , base=base, target_name = 'SCPTool')
]

setup(name='SCP-Tool',
      version = '1.1',
      description = 'A simple Tool in Python to help you make an SCP syntax',
      options = {'build_exe': build_options},
      executables = executables)
