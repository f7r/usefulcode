# =============================================================================
# Author: falseuser
# Created Time: 2019-01-09 17:18:58
# Last modified: 2019-01-09 17:29:44
# Description: path.py
# =============================================================================
import os
import pathlib


def get_runtime_path2():
    return os.path.dirname(os.path.realpath(__file__))


# For python3
def get_runtime_path3():
    p = pathlib.Path(__file__)
    return str(p.resolve().parent)


if __name__ == "__main__":
    print(get_runtime_path2())
    print(get_runtime_path3())
