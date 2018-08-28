import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

a = pd.DataFrame({ 'metric_path' : np.repeat('A',500), 'value': np.random.normal(10, 5, 500), 'time' : np.arange(500) })
b = pd.DataFrame({ 'metric_path' : np.repeat('B',500), 'value': np.random.normal(13, 1.2, 500), 'time' : np.arange(500) })
c = pd.DataFrame({ 'metric_path' : np.repeat('B',500), 'value': np.random.normal(18, 1.2, 500), 'time' : np.arange(500) })
d = pd.DataFrame({ 'metric_path' : np.repeat('C',20),  'value': np.random.normal(25, 4, 20), 'time' : np.arange(20) })
e = pd.DataFrame({ 'metric_path' : np.repeat('D',100), 'value': np.random.uniform(12, size=100), 'time' : np.arange(100) })

f = pd.DataFrame({ 'metric_path' : np.repeat('A',500),'value': np.random.normal(10, 5, 500), 'time' : np.arange(500) })
g = pd.DataFrame({ 'metric_path' : np.repeat('B',500),'value': np.random.normal(13, 1.2, 500), 'time' : np.arange(500) })
h = pd.DataFrame({ 'metric_path' : np.repeat('B',500),'value': np.random.normal(18, 1.2, 500), 'time' : np.arange(500) })
i = pd.DataFrame({ 'metric_path' : np.repeat('C',20), 'value': np.random.normal(25, 4, 20), 'time' : np.arange(20) })
j = pd.DataFrame({ 'metric_path' : np.repeat('D',100),'value': np.random.uniform(12, size=100), 'time' : np.arange(100) })

df_1= a.append(b).append(c).append(d).append(e)
df_2 =f.append(g).append(h).append(i).append(i)

df1= a.append(b).append(c).append(d).append(e)
df2 =f.append(g).append(h).append(i).append(i)

df1_quantile = df_1.groupby('metric_path').value.quantile(.90)
df2_quantile = df_2.groupby('metric_path').value.quantile(.90)

merge_quantile = df1_quantile.combine(df2_quantile, lambda x1, x2: True if x1 < x2 else False)
merge_quantile = pd.concat([df1_quantile, df2_quantile], axis=1)
merge_quantile.columns = ['test1','test2']
merge_quantile['test'] = merge_quantile['test1'] < merge_quantile['test2']

df3['test'] = df3['value_x'] < df3['value_y']
df3 = df3.loc[df3.test.isin([True])]

z1 = df3[['metric_path', 'value_x', 'value_y']].groupby('metric_path').transform(
lambda group: (group.index.value_x.quantile(0.90) - group.value_y.quantile(0.90))
)


df1_quantile = df_1.groupby('metric_path').value.quantile(.90)
df2_quantile = df_2.groupby('metric_path').value.quantile(.90)

for read in df1_quantile:
    print(read.index)
    print('end')
    for ref in ref.itertuples():
        if abs(read[1]-ref[2]) <= 10:
            print(str(read[0])+' match '+str(ref[1]))
        else:
            print(str(read[0])+' match None')



np.random.seed(0)
nb_sample = 100
num_sample = (0,100)

d = dict()
d['User_id'] = np.random.randint(num_sample[0], num_sample[1], nb_sample)
for i in range(5):
    d['Col' + str(i)] = np.random.randint(num_sample[0], num_sample[1], nb_sample)

df = pd.DataFrame.from_dict(d)
filt_df = df.loc[:, df.columns != 'User_id']
low = .05
high = .95
quant_df = filt_df.quantile([low, high])
print(quant_df)
filt_df = filt_df.apply(lambda x: x[(x>quant_df.loc[low,x.name]) & (x < quant_df.loc[high,x.name])], axis=0)

z = df_1[['metric_path','value']].groupby('metric_path').transform(
lambda group: group - (group.quantile(0.75)+( group.quantile(.75)-group.quantile(.25) ) *1.5) 
)
outliers = z > 0.0
df_1[outliers.any(axis=1)]
