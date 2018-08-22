import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

### Teste de exibicao
#%%>
fig, ax = plt.subplots(figsize=(11.7, 8.27))
diamonds = sns.load_dataset("diamonds")
#sns.catplot(x="color", y="price", kind="boxen",
#            data=diamonds.sort_values("color"))
sns.boxplot(x='color', y='price', data=diamonds.sort_values("color"), ax=ax)


### Teste de regex metric_path
re.sub(pattern='^(Backends\|Discovered backends call - |Backends\|)([A-Za-z\d -:\/\.]+)\|.*',repl=r'\2', string='Backends|Discovered backends call - API-IB - http://localhost:80/Depositos|Average Wait Time (ms);')
re.sub(pattern='^(Backends\|Discovered backends call - |Backends\|)([A-Za-z\d -:\/\.]+)\|.*',repl=r'\2', string='Backends|APP-TRANSACAO|Average Wait Time (ms);')

### Teste de merge do dataset
#%%>
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

result = df_1.merge(df_2, on=['metric_path','time'], how='inner')

df_1 = df_1.set_index(['metric_path','time'])
df_2 = df_2.set_index(['metric_path','time'])

sns.lmplot(x="value_x", y="value_y", hue="metric_path",fit_reg=False, data=result)

#%%>
### Teste tratamento de Data
test = pd.read_csv("data/test_itau.csv", sep = ";", header = None)
test.columns = ['metricPath','frequency', 'value', 'current', 'min', 'max', 'count', 'time']
test['time'] = pd.to_datetime(test['time'], unit = 'ms')
test = test.set_index('time')

test.between_time('22:00', '23:00')

### Teste para pegar os Outliers
df = pd.DataFrame({'metric_path': ['M','M','M','F','F','F','F'], 'value_x': [33,42,19,64,12,30,32], 'value_y': ['163','167','184','164','162','158','160'],})
df['value_y'] = df['value_y'].astype(float)
stds = 1.0
z = df[['metric_path', 'value_y', 'value_x']].groupby('metric_path').transform(
    lambda group: (group - group.mean()).div(group.std()))
outliers = z.abs() > stds
outliers

df[outliers.any(axis=1)]

#%%>
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

g = sns.FacetGrid(df, col="origin") 
g.map(sns.regplot, "horsepower", "mpg") 
plt.xlim(0, 250) 
plt.ylim(0, 60)

#%%>
import seaborn as sns; sns.set(color_codes=True)
tips = sns.load_dataset("tips")
g = sns.lmplot(x="total_bill", y="tip", data=tips)