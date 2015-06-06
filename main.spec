# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=[''],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ResponsiveLayoutCreator.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon = 'resources\\ResponsiveLayout.ico',
          version = 'version.txt' )

##### include other directory in distribution #######
def extra_datas(data_directory):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % data_directory, files)
    extra_datas = []
    for f in files:
        if not (f.endswith(".ico") or f.endswith(".png")):
            extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################

# append the required directories
a.datas += extra_datas('resources')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='ResponsiveLayoutCreator')
