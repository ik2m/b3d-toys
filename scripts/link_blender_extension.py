#!/usr/bin/env python3
from pathlib import Path
import shutil
import os
import sys

if os.name != "nt":
    print("このスクリプトは Windows 専用です。中断します。")
    sys.exit(1)

# Blender 拡張機能の user_default フォルダ
ext_path = Path.home() / "AppData/Roaming/Blender Foundation/Blender/4.2/extensions/user_default/b3d_toys"

# 開発中のリポジトリ内ソース
src_path = Path(__file__).parent.parent / "src" / "b3d_toys"

# 既存のリンクやフォルダを削除
if ext_path.exists() or ext_path.is_symlink():
    if ext_path.is_dir():
        shutil.rmtree(ext_path)
    else:
        ext_path.unlink()

# シンボリックリンク作成
try:
    os.symlink(src_path, ext_path, target_is_directory=True)
    print(f"Linked {src_path} -> {ext_path}")
except OSError as e:
    print("シンボリックリンクの作成に失敗しました:", e)
    sys.exit(1)
