import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("The cli was called with arguments: " + str(args._))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
