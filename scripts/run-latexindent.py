#!/usr/bin/env python3

import os
import subprocess
from sys import argv

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR_PATH = os.path.abspath(THIS_DIR + "/../.latexindent")


def run_latexindent(filepath: str):
    """latexindent を適用する。

    Args:
        filepath (str): ファイルパス
    """

    os.makedirs(TMP_DIR_PATH, exist_ok=True)

    subprocess.run(
        [
            "latexindent",
            "-w",  # 上書きする。
            "-l",  # ローカルの設定ファイルを読み込む。
            "-s",  # フォーマット結果を標準出力しない。
            "-c",
            TMP_DIR_PATH,  # 一時ファイルを .latexindent に出力する。
            filepath,
        ],
        check=True,
    )


if __name__ == "__main__":
    filepaths = argv[1:]
    for filepath in filepaths:
        run_latexindent(filepath)
