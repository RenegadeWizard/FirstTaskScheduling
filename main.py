from Generator import Generator
from Validator import Validator

FILE_NAME = "out/out.txt"


def main():
    Generator(5).serialize(FILE_NAME)
    Validator(FILE_NAME, "")


if __name__ == '__main__':
    main()
