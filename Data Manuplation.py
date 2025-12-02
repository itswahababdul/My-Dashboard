#Data_cleaning.py
import pandas as pd
url="https://people.sc.fsu.edu/-jburkardt/data/csv/hw_200.csv"
df=pd.read_csv(url)
#cleaning example
df.dropna(inplace=True)
df.columns=[cool.strip().replace('','_')for col in df.columns]
#save cleaned data
df.to_csv("cleanes1_data.csv",index=False)
print("Data Cleaned and Saved.")
