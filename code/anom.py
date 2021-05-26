'''
Isolation Forest Anomaly detection script

Sandy Herho <herho@umd.edu>
2021/05/24
'''

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pycaret.anomaly import *

df = pd.read_csv("https://raw.githubusercontent.com/sandyherho/natunaRainStatAnal/main/data/prInterp.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', drop=True, inplace=True)

s = setup(df, session_id = 123)

iforest = create_model('iforest')
iforest_results = assign_model(iforest)

anom = iforest_results[iforest_results['Anomaly'] == 1]
anom.to_csv('./data/anom_precip.csv')

fig = px.line(iforest_results, x=iforest_results.index, y="precipitation",
              labels = {'precipitation': 'precipitation (mm/day)',
                        'x' : 'time'}, 
              template = 'plotly_dark')

outlier_dates = iforest_results[iforest_results['Anomaly'] == 1].index

y_values = [iforest_results.loc[i]['precipitation'] for i in outlier_dates]

fig.add_trace(go.Scatter(x=outlier_dates, y=y_values, mode = 'markers', 
                name = 'Anomaly', 
                marker=dict(color='red',size=10)))
