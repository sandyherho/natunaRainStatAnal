'''
Piecewise Cubic Hermite Interpolating Polynomial script

Sandy Herho <herho@umd.edu>
2021/05/24
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (20, 8)
plt.style.use('ggplot')

df = pd.read_csv('https://raw.githubusercontent.com/sandyherho/natunaRainStatAnal/main/data/daily_data.csv')

pr = df['pr'].interpolate(method='pchip')
t = pd.to_datetime(df['date'], dayfirst=True)

plt.plot(t, pr, '#1f91a1');
plt.ylabel('precipitation (mm/day)');
plt.xlabel('time');
plt.ylim(0, 200);
plt.tight_layout();
plt.savefig('./figs/fig2.png')
