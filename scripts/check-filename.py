#!/usr/bin/env python3

import re
from sys import argv

FILENAME_REGEX = re.compile(r"^[a-zA-Z0-9./-]*$")


def check_filename(filepath: str):
    if not FILENAME_REGEX.match(filepath):
        raise ValueError("Invalid filepath: " + filepath)


if __name__ == "__main__":
    for arg in argv[1:]:
        check_filename(arg)
