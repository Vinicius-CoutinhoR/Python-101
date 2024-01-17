import math
import sys
import errno


class TerminalColor:
    ERROR_COLOR = '\033[91m'
    DEFAULT_COLOR = '\033[0m'


def circunference(radius):
    return math.pi * (math.pow(float(radius), 2))


def help():
    print(TerminalColor.ERROR_COLOR,
          'You must enter the argument on the command line!')
    backslash = '\\'
    fileName = sys.modules[__name__].__file__.split(backslash)[-1]
    print(f"Syntax: { fileName } <int: radius>")
    print(TerminalColor.DEFAULT_COLOR)


if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERROR_COLOR,
              'The radius must be a numerical value!',
              TerminalColor.DEFAULT_COLOR)
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    print(f'The circunference area is: { round(circunference(radius), 2) }')
