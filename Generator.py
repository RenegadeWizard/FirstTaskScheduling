import random
from Task import Task

MAX_RANGE = 30  # TODO: ??


class Generator:
    def __init__(self, tasks_number):
        self.tasks = []
        for _ in range(tasks_number):
            self.append_task()

    def append_task(self):
        p = random.randint(1, MAX_RANGE)
        r = random.randint(1, MAX_RANGE)
        d = random.randint(r + 1, MAX_RANGE + 1)
        w = random.randint(1, MAX_RANGE)
        self.tasks.append(Task(p, r, d, w))

    def serialize(self, file_name):
        with open(file_name, 'w') as file:
            for task in self.tasks:
                file.write(str(self.tasks.index(task) + 1) + "\n")
                file.write(str(task) + "\n")
