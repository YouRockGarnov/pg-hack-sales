from Data_clean import Data_clean
import pandas as pd


def main():
    cleaner_obj = Data_clean('../db.xlsx',['Category','Brand','Line Up'],1)
    cleaner_obj.metric()
    cleaned = cleaner_obj.get_data()
    cleaned.rename(columns={
        "Base NIV": "bNIV",
        "Base NOS": "bNOS",
        "iNOS, line-up": "iNOSl",
        "ROI , line-up": "ROIl",
        "Volume, IT": "Vol",
        "Base Volume, IT": "bVol"
    })
    cleaned.to_csv("./cl.csv")


if __name__ == "__main__":
    main()
