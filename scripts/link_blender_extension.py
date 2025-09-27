#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import shutil

# Windows 専用判定
if os.name != "nt":
    print("このスクリプトは Windows 専用です。中断します。")
    sys.exit(1)

# Blender 拡張機能フォルダ (user_default)
ext_path = Path.home() / "AppData/Roaming/Blender Foundation/Blender/4.2/extensions/user_default/b3d_toys"

# 開発中のリポジトリ内ソース
src_path = Path(__file__).parent.parent / "src" / "b3d_toys"

# 既存のリンクやフォルダを削除
if ext_path.exists() or ext_path.is_symlink():
    if ext_path.is_symlink():
        ext_path.unlink()  # シンボリックリンクは unlink
    elif ext_path.is_dir():
        shutil.rmtree(ext_path)
    else:
        ext_path.unlink()  # ファイルの場合

# シンボリックリンク作成
try:
    os.symlink(src_path, ext_path, target_is_directory=True)
    print(f"シンボリックリンクを作成しました。： {src_path} -> {ext_path}")
except OSError as e:
    print(f"シンボリックリンクの作成に失敗しました: {e}")
    sys.exit(1)

