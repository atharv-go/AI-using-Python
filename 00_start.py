# %%

# how to open a file 
import os
import pandas as pd

# TYPE 1 
print(f"Current working directory is: {os.getcwd()}")

data_path= "../../sales-analysis/data/sales.csv"

if os.path.exists(data_path):
    print("Data is accessible")
else :
    print("Data is not accessible")

df=pd.read_csv("../../sales-analysis/data/sales.csv")
print(df)

# ---------------------

# TYPE 2

with open('../../sales-analysis/data/sales.csv','r') as f:
    dff = f.read()
print(dff)

# with open just opens the file as it is whereas if we use proper pandas library function read_csv it opens in csv format