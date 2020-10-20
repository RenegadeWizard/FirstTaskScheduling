class Result:
    def __init__(self, u: int, tasks: [int]):
        self.u = u
        self.tasks = tasks

    def __str__(self):
        return str(self.u) + ' ' + str(self.tasks)

    def __repr__(self):
        return self.__str__()
