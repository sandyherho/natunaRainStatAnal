'''
Monthly average precipitation script

Sandy Herho <herho@umd.edu>
2021/05/28
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

url = 'https://raw.githubusercontent.com/sandyherho/natunaRainStatAnal/main/data/prInterp.csv'
data = pd.read_csv(url, index_col='date', parse_dates=True)

df = data.resample('MS').sum()
df.to_csv('../data/avemonth.csv')

fig, ax = plt.subplots(figsize=(20, 8))
df.groupby(df.index.month)["precipitation"].mean().plot(kind='bar', 
                                                        color='#0f82d4', 
                                                        rot=0, ax=ax);
ax.set_xlabel('month');
ax.set_ylabel('precipitation (mm/month)');

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticklabels(labels);