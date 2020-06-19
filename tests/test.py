import os
import subprocess
import sys
import unittest


class TestMain(unittest.TestCase):

    def test_who(self):
        args = [
            sys.executable,
            os.path.join(os.path.dirname(__file__), os.pardir, 'src', 'win32sys.py'),
            'whoami',
            '|',
            'findstr',
            '\"nt authority\\system\"'
        ]

        cmd = ' '.join(args)
        assert os.system(cmd) == 0


if __name__ == '__main__':
    unittest.main()
