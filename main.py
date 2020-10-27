from service.Generator import Generator
from service.Validator import Validator

OUT_FILE_NAME = "out/out.txt"
IN_FILE_NAME = "out/in.txt"


def main():
    test = list(range(50, 501, 50))
    # indexy = ['136774', '136785', '136812', '136815', '132336', '136803', '132639', '136814', '136807', '136798',
    #           '132337', '132321', '136808', '136691']
    indexy = ['136807']
    algorithm = "/home/krzysztof/Dokumenty/Studia/semestr7/Szeregowanie/zadanie1_algorytm/cmake-build-debug/zadanie1_algorytm"
    for index in indexy:
        print(f"\n{index}\n")
        for i in test:
            print(f"{i}\t:\t", end='')
            Validator(
                f"/home/krzysztof/Dokumenty/Studia/semestr7/Szeregowanie/instancje/in_{index}/in_{index}_{i}.txt",
                algorithm).execution()


if __name__ == '__main__':
    main()
