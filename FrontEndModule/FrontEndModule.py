from Components.InputComponent.InputComponent import InputComponent
from Components.OutputComponent.OutputComponent import OutputComponent


class FrontEndModule:
    def __init__(self):
        self.input_module = InputComponent()
        self.output_module = OutputComponent()
        self.input_module.add_ebox('pandgine@gmail.com', 'dreamTeam13', "imap.gmail.com", 993)

    def get_input(self):
        return self.input_module.get_input_from_ebox('pandgine@gmail.com')

    def send_output(self, csv_file_path_from_outcomp):
        self.output_module.put_csv_file_to_output('prediction.xlsx', csv_file_path_from_outcomp=csv_file_path_from_outcomp)
        self.output_module.send_mess()

