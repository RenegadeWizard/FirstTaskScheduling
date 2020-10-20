import random
from model.Task import Task

MAX_DURATION = 30
MAX_START = 30
MAX_WEIGHT = 10


class Generator:
    def __init__(self, tasks_number):
        self.tasks = []
        for _ in range(tasks_number):
            self.__append_new_task()

    def serialize(self, file_name):
        with open(file_name, 'w') as file:
            file.write(str(len(self.tasks)) + '\n')
            for task in self.tasks:
                file.write(str(task) + '\n')

    def __append_new_task(self):
        p = random.randint(1, MAX_DURATION)
        r = random.randint(1, MAX_DURATION)
        d = random.randint(r + p + 1, r + 2 * MAX_DURATION + 1)
        w = random.randint(1, MAX_WEIGHT)
        self.tasks.append(Task(p, r, d, w))
