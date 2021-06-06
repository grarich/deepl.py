import argparse
import platform
import sys

import aiohttp
import requests

import deepl


def main():
    parser = argparse.ArgumentParser(prog='deepl', description='CLI tool for deepl.py')
    parser.add_argument('-v', '--version', action='store_true', help='shows the library version.')
    args = parser.parse_args()
    if args.version:
        print(f'- Python v{sys.version}')
        print(f'- deepl.py v{deepl.__version__}')
        print(f'- aiohttp v{aiohttp.__version__}')
        print(f'- requests v{requests.__version__}')

        print('- System Info: {0.system} {0.release} {0.version}'.format(platform.uname()))


if __name__ == '__main__':
    main()
