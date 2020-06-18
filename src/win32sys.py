import subprocess
import sys
import os

assert sys.platform == 'win32', 'This application can be build and run on win32 platform only.'


def run_as_system(*args, **kwargs):
    """
    :param args: arguments that are directly forwarded to subprocess.call()
    :param kwargs: optional keyword arguments that are directly forwarded to subprocess.call()
    :return:
    """

    ps_exec = 'PsExec.exe'
    if getattr(sys, 'frozen', False):
        ps_exec = os.path.join(os.path.dirname(__file__), ps_exec)
    else:
        ps_exec = os.path.join(os.path.dirname(__file__), '..', 'lib', ps_exec)

    completed_args = [ps_exec, '-s', '-i']
    if os.system('where ' + args[0]) != 0:
        # not an executable
        completed_args.extend(['cmd', '/c', 'cd', os.getcwd(), '&'])

    completed_args.extend(args)
    return subprocess.call(completed_args, **kwargs)


if __name__ == '__main__':
    sys.exit(run_as_system(*sys.argv[1:]))
