class Task:
    def __init__(self, p, r, d, w):
        self.p = p  # TODO: rozwiń nazwy
        self.r = r
        self.d = d
        self.w = w

    def __str__(self):
        return str(self.p) + " " + str(self.r) + " " + str(self.d) + " " + str(self.w)
