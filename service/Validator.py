import subprocess
from datetime import datetime

from model.Result import Result
from model.Task import Task


class Validator:
    def __init__(self, input_file_name: str, result_file_name: str):
        self.execution = self.validate_result
        self.input = input_file_name
        self.output = result_file_name
        self.__check_output_file(result_file_name)

    def validate_result(self):
        tasks = self.__parse_input(self.input)
        result = self.__parse_output(self.output)
        self.__validate(result, tasks)

    def validate_algorithm(self):
        time_start = datetime.now()
        process = subprocess.run(self.output)
        time_end = datetime.now()
        # tasks = self.__parse_input(self.input)    # TODO
        # result = self.__parse_output(self.output)
        # self.__validate(result, tasks)
        print(process.stdout)
        print(f"time: {(time_end - time_start).microseconds / 1000} ms")

    def __validate(self, result, tasks):
        weight_sum = 0
        time = 0
        if len(tasks) != len(result.tasks):
            print("Incorrect number of tasks!")
            return
        for task in result.tasks:
            curr_task = tasks[task - 1]
            time = max(time + 1, curr_task.ready_time) + curr_task.processing_time
            if time > curr_task.due_time:
                weight_sum += curr_task.weight
        # if weight_sum == result.u:    # PROD
        #     print("Correct")
        # else:
        #     print("Incorrect")
        print(weight_sum)

    def __check_output_file(self, file_name: str):
        if file_name.rfind('.txt') > 0:
            self.execution = self.validate_result
        else:
            self.execution = self.validate_algorithm

    @staticmethod
    def __parse_input(input_file_name) -> [Task]:
        with open(input_file_name, 'r') as file:
            input_file_tab = file.read().split('\n')
        tasks = []
        for i in range(int(input_file_tab[0])):
            tasks.append(Task.of([int(i) for i in input_file_tab[i + 1].split(' ')]))
        return tasks

    @staticmethod
    def __parse_output(output_file_name) -> Result:
        with open(output_file_name, 'r') as file:
            output_file = file.read().split('\n')
        return Result(int(output_file[0]), [int(i) for i in output_file[1].split(' ') if i != ''])
