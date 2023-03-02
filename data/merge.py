import pandas as pd
import os

df =[]

# li = os.getcwd()
# print(li)
for files in os.listdir('data'): 
    # print(files)
    if files.find('description')>-1:
        data = pd.read_csv(f'data/{files}')
        df.append(data)
        
df = pd.concat(df)
df.to_csv('data/final_data.csv',index=False)