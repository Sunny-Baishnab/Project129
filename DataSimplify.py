import csv
from os import replace
import pandas as pd

df1 = []

df1 = pd.read_csv('brownstars.csv')

df1 = df1[df1["distance"].notna()]
df1 = df1[df1["mass"].notna()]
df1 = df1[df1["radius"].notna()]

df1["mass"] = df1["mass"].apply(lambda x: x.replace('$','').replace(',','')).astype('float')

df1["radius"] = 0.102763 * df1["radius"]
df1["mass"] = 0.000954588 * df1["mass"]

df1.to_csv('simplified.csv')