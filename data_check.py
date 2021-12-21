import pandas as pd 
import glob

path = glob.glob('*.json')

df = pd.read_json(path[0],encoding="utf-8")

print(df)
