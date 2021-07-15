#!/usr/bin/env python3

import pathlib
import logging
import re

logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__file__)

ENCODING = 'utf8'
SUCCESS = True


def fix_ten_maru(filepath: str):
    """句読点を修正する

    Args:
        filepath (str): ファイルパス
    """

    with open(filepath, mode='r', encoding=ENCODING) as file:
        contents = file.read()

    fixed_contents = contents.replace('、', '，').replace('。', '．')
    if contents != fixed_contents:
        LOGGER.warning('fixed ten maru in a file %s', filepath)
        global SUCCESS
        SUCCESS = False

    with open(filepath, mode='w', encoding=ENCODING) as file:
        file.write(fixed_contents)


def check_file(filepath: pathlib.Path):
    """ファイルをチェックする

    Args:
        filepath (pathlib.Path): ファイルパス
    """

    LOGGER.debug('check a file %s', filepath)
    fix_ten_maru(str(filepath))


IGNORE_DIR_REGEX = re.compile(R'\.git|extern')
TEX_FILE_SUFFIX = '.tex'


def fix_in_dir(dirpath: pathlib.Path):
    """ディレクトリ内のファイルを修正する

    Args:
        dirpath (pathlib.Path): ディレクトリパス
    """

    LOGGER.debug('search in directory %s', dirpath)
    for child in dirpath.iterdir():
        if child.is_dir() and not IGNORE_DIR_REGEX.search(str(child)):
            fix_in_dir(child)
        if child.is_file() and str(child).endswith(TEX_FILE_SUFFIX):
            check_file(child)


def fix_all():
    """全ファイルを修正する
    """

    this_dir = pathlib.Path(__file__).parent
    fix_in_dir(this_dir)

    if not SUCCESS:
        LOGGER.warning('some files are fixed')
        exit(1)

    LOGGER.info('no file changed')


if __name__ == '__main__':
    fix_all()
