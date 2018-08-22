import os

script_dir = os.path.dirname(__file__) 
rel_path = '..\\resource\\trasac_online_retail.csv'
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path)
 
import csv

csvread = csv.reader(file,delimiter=';')

from apyori import apriori

results = list(apriori(csvread))

for result in results:
    print (result)

import pandas as pd  

s = pd.Series(["a","b","c","a"], dtype="category")

df = pd.DataFrame({"A":["a","b","c","a"]})


pd_readcsv = pd.read_csv(file)