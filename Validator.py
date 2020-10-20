from model.Result import Result
from model.Task import Task


class Validator:
    def __init__(self, input_file_name: str, result_file_name: str):
        self.execution = self.validate_result
        self.input = input_file_name
        self.output = result_file_name
        self.__check_output_file(result_file_name)
        self.execution()

    def __check_output_file(self, file_name: str):
        if file_name.rfind('.txt') > 0:
            self.execution = self.validate_result
        else:
            self.execution = self.validate_algorithm

    def validate_result(self):
        tasks = self.__parse_input()
        result = self.__parse_output()

    def validate_algorithm(self):
        pass  # TODO: zaimplementuj

    def __parse_input(self) -> [Task]:
        with open(self.input, 'r') as file:
            input_file_tab = file.read().split('\n')
        tasks = []
        for i in range(int(input_file_tab[0])):
            tasks.append(Task.of(input_file_tab[i + 1].split(' ')))
        return tasks

    def __parse_output(self) -> Result:
        with open(self.output, 'r') as file:
            output_file = file.read().split('\n')
        return Result(int(output_file[0]), [int(i) for i in output_file[1].split(' ')])
