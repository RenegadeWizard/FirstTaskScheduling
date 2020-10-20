from service.Validator import Validator

OUT_FILE_NAME = "out/out.txt"
IN_FILE_NAME = "out/in.txt"


def main():
    # Generator(5).serialize(FILE_NAME)
    Validator(OUT_FILE_NAME, IN_FILE_NAME)


if __name__ == '__main__':
    main()
