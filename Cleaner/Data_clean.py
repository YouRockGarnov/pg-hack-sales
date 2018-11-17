import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Data_clean():

    def __init__(self,name_data,columns : list,flag):
        self.name_data = name_data
        self.columns = columns
        self.flag = flag
        self.data = pd.read_excel(name_data)
        self.data = self.data[columns]
        #self.data = self.data[self.data['Promo flag'] == flag]

    def metric(self):
        label = LabelEncoder()

        dicts = {}
        for column in self.columns:
            label.fit(self.data[column].drop_duplicates())  # задаем список значений для кодирования
            dicts[column] = list(label.classes_)
            self.data[column] = label.transform(self.data[column])  # заменяем значения из списка кодами закодированных элементов

    def get_data(self):
        return self.data

