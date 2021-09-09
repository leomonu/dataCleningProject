import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
del df["luminosity"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
