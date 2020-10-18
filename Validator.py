class Validator:
    def __init__(self, input_file_name, result_file_name):
        self.execution = self.validate_result
        self.input = input_file_name
        self.output = result_file_name
        self.check_output_file(result_file_name)
        self.execution()

    def check_output_file(self, file_name):
        if file_name == "":  # TODO: zaimplementuj
            self.execution = self.validate_result
        else:
            self.execution = self.validate_algorithm

    def validate_result(self):
        pass

    def validate_algorithm(self):
        pass  # TODO: zaimplementuj
