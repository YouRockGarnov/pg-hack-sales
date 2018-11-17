from Components.InOutputComponent import InOutComponent
from Converters.ConverterCSVToExcel import ConverterCSVToExcel
from Components.OutputComponent.EmailSender import EmailSender
import pandas as pd

class OutputComponent(InOutComponent):
    def send_mess(self):
        es = EmailSender() # OutputComponent.eboxes['hamta@yandex.ru']) -> IT MUST BE.
        es.send_mes(self.file_path, whom='hamta@yandex.ru')

    def put_csv_file_to_output(self, output_file_path, csv_file_path_from_outcomp):
        self.file_path = output_file_path
        converter = ConverterCSVToExcel()

        csv_file = pd.read_csv(csv_file_path_from_outcomp)
        writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')
        csv_file.to_excel(writer, sheet_name='Prediction')
        writer.save()