class Task:
    def __init__(self, p, r, d, w):
        self.p = p  # TODO: rozwiń nazwy
        self.r = r
        self.d = d
        self.w = w

    @staticmethod
    def of(tab):
        return Task(tab[0], tab[1], tab[2], tab[3])

    def __str__(self):
        return str(self.p) + " " + str(self.r) + " " + str(self.d) + " " + str(self.w)

    def __repr__(self):
        return self.__str__()
