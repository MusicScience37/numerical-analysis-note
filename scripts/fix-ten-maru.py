#!/usr/bin/env python3

from sys import argv

ENCODING = "utf8"


def fix_ten_maru(filepath: str):
    """句読点を修正する

    Args:
        filepath (str): ファイルパス
    """

    with open(filepath, mode="r", encoding=ENCODING) as file:
        contents = file.read()

    fixed_contents = contents.replace("、", "，").replace("。", "．")
    if contents != fixed_contents:
        print(f"Fixing {filepath}")

    with open(filepath, mode="w", encoding=ENCODING) as file:
        file.write(fixed_contents)


if __name__ == "__main__":
    filepaths = argv[1:]
    for filepath in filepaths:
        fix_ten_maru(filepath)
