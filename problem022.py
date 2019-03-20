import pandas as pd 

namelist = pd.read_csv("p022_names.txt")

namelist.columns.tolist()
namelist.sort()

print(namelist)