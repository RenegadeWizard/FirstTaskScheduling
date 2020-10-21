class Task:
    def __init__(self, p: int, r: int, d: int, w: int):
        self.processing_time = p
        self.ready_time = r
        self.due_time = d
        self.weight = w

    @staticmethod
    def of(tab):
        return Task(tab[0], tab[1], tab[2], tab[3])

    def __str__(self):
        return str(self.processing_time) + " " + str(self.ready_time) + " " + str(self.due_time) + " " + str(
            self.weight)

    def __repr__(self):
        return self.__str__()
