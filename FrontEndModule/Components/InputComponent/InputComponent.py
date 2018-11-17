from Components.EmailBox import EmailBox
from Converters.ConverterRowsToCSV import ConverterRowsToCSV
from Components.InOutputComponent import InOutComponent

class InputComponent(InOutComponent):
    def __init__(self):
        pass

    def get_input_from_ebox(self, ebox_adress):
        # for ebox in self.eboxes.values():
        #     ebox.read_email_from_gmail()

        converter = ConverterRowsToCSV()
        rows = InOutComponent.eboxes[ebox_adress].read_email_from_gmail()
        return converter.rows_to_csv(rows)