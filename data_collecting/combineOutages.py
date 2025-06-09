import pandas as pd
import os
import sys

# OTC Plant Codes that were found in the Outage Data
otcs = [
            "ALAMIT_2_PL1X3", "ALAMIT_7_UNIT 3","ALAMIT_7_UNIT 4","ALAMIT_7_UNIT 5",
            "HNTGBH_2_PL1X3", "HNTGBH_7_UNIT 2", "ORMOND_7_UNIT 1",
            "ORMOND_7_UNIT 2", "HARBGN_7_UNITS", "MOSSLD_2_PSP1", "MOSSLD_2_PSP2"]

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

combined_data = []

# Loops through each month directory and processes the files
for month in months:
    fileDir = f"./{month}"
    files = os.listdir(fileDir)
    for file in files:
        print(f"\rProcessing file: {file}", end="")
        data = pd.read_excel(f"{fileDir}/{file}", header=9)
        data.drop(labels=['Unnamed: 0', 'Unnamed: 3', 'Unnamed: 11'], inplace=True, axis=1)
        combined_data.append(data)

print("\nCombining data...")

# Merge into one csv
combined_data = pd.concat(combined_data, ignore_index=True)
combined_data.drop_duplicates(inplace=True)
combined_data.dropna(inplace=True)
combined_data['isOTC'] = combined_data["RESOURCE ID"].isin(otcs)
combined_data.to_csv("FullOutageData.csv", index=False)

print("FullOutageData.csv created")