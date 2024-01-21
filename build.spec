# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['src/mainUI.py'],
             pathex=['.'],  # Указывает пути поиска для всех необходимых модулей
             binaries=[],
             datas=[('src/assets/*', 'assets'),  # Включает папку assets в конечную сборку
                    ('src/oracle/*', 'oracle')],  # Включает папку oracle
             hiddenimports=[],  # Здесь можно указать скрытые импорты
             hookspath=[],
             runtime_hooks=[],
             excludes=[],  # Здесь можно исключить ненужные модули
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Buisness-Calc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,  # Графическое приложение, не нужна консоль
          icon='src/assets/online-shop-_1_.ico',  # Указываем иконку приложения
          version=None,
          manifest=None)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Buisness-Calc-1.0.1')