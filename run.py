import argparse
import os
import sys

from parser.reader import read
from parser.writer import write


def _create_dir():
    """Creates out dir."""
    cwd = os.getcwd()
    to = os.path.join(cwd, "out")
    if not os.path.exists(to):
        os.mkdir(to)
    return to


def _parse_args():
    """Parse args."""
    parser = argparse.ArgumentParser(
        description='Parse xls file '
                    'into several csv files to ./out')
    parser.add_argument('filepath', type=str, help='File path')
    return parser.parse_args()


def main():
    filepath = _parse_args().filepath
    filename = filepath.split(os.path.sep)[-1]

    if not os.path.exists(filepath):
        sys.stdout.write(f"File not found {filepath}. Exit")
        return

    frames = read(filepath)

    out_dir = _create_dir()

    results = write(out_dir, filename, frames)
    out_files = "\n- ".join(results)
    sys.stdout.write(f"Successfully parsed to:\n- {out_files}")


if __name__ == '__main__':
    main()
