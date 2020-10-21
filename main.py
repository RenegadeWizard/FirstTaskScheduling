from service.Generator import Generator
from service.Validator import Validator

OUT_FILE_NAME = "out/out.txt"
IN_FILE_NAME = "out/in.txt"


def main():
    test = list(range(50, 501, 50))
    # test.remove(400)
    # test = [100]
    for i in test:
        print(f"{i}\t:\t")
        Generator(i).serialize(f"out/in_136807_{i}.txt")
        # Validator(f"out/bartek/in_136798_{i}.txt", f"out/in/test{i}.txt").execution()


if __name__ == '__main__':
    main()
