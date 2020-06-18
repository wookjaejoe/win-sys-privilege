import os
import subprocess
import sys
import unittest


class TestMain(unittest.TestCase):

    def test_who(self):
        # noinspection SpellCheckingInspection,PyTypeChecker
        subprocess.check_call(args=[sys.executable, 'win32sys.py', 'whoami', '|', 'findstr', 'nt authority\system'],
                              cwd=os.path.join(os.path.dirname(__file__), '..', 'src'))


if __name__ == '__main__':
    unittest.main()
