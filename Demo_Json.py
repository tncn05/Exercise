import pandas as pd

df=pd.read_json("../datasets/SalesTransactions.json",
               encoding='utf-8', dtype='unicode')

print(df)