import pandas as pd

class ConverterRowsToCSV:
    def rows_to_csv(self, rows):
        return pd.DataFrame(rows)