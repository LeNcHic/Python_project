import pandas as pd


df = pd.read_csv('/Users/leonidlevin/Downloads/Python_project/Python_project/python_project_belman_ford//data/rates')
df = df.reset_index()
arr_rates = []
for index, row in df.iterrows():
    new_rate = []
    new_rate.append(row[1:7])
    new_rate.append(row[7:13])
    new_rate.append(row[13:19])
    new_rate.append(row[19:25])
    new_rate.append(row[25:31])
    new_rate.append(row[31:37])
    arr_rates.append(new_rate)
