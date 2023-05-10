import pandas as pd


df = pd.read_csv('/Users/leonidlevin/Downloads/Python_project/Python_project/python_project_belman_ford//data/rates')
df = df.reset_index()
arr_rates = []
for index, row in df.iterrows():
    new_rate = []
    new_rate.append(row[1:7])
    new_rate.append(row[6:13])
    new_rate.append(row[12:19])
    new_rate.append(row[18:25])
    new_rate.append(row[24:31])
    new_rate.append(row[30:37])
    arr_rates.append(new_rate)
