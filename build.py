import os
import sys
import subprocess
from distutils.dir_util import copy_tree
import shutil

assert sys.platform == 'win32', 'This application can be build and run on win32 platform only.'

root_dir = os.path.dirname(__file__)


def build():
    dist_dir = os.path.join(root_dir, 'dist', 'win32sys')
    for _ in range(10):
        shutil.rmtree(dist_dir, ignore_errors=True)

    # noinspection SpellCheckingInspection
    subprocess.check_call(args=['pyinstaller', os.path.join(root_dir, 'src', 'win32sys.py')])
    copy_tree(os.path.join(root_dir, 'lib'), dist_dir)


if __name__ == '__main__':
    build()
