from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'SCP-Tool')
]

setup(name='SCP Generator',
      version = '1.0',
      description = 'A simple Tool in Python to help you make an SCP syntax',
      options = {'build_exe': build_options},
      executables = executables)
