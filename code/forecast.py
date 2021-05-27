'''
Empirical forecasting with FbProphet
Sandy Herho <herho@umd.edu>

05/27/2021
'''
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot
plt.style.use('ggplot')

url = "https://raw.githubusercontent.com/sandyherho/natunaRainStatAnal/main/data/prInterp.csv"
data = pd.read_csv(url)

df = pd.DataFrame()
df['ds'] = pd.to_datetime(data['date'])
df['y'] = data['precipitation']

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=3 * 30, freq='D')

forecast = m.predict(future)

fig = m.plot(forecast, xlabel='time', ylabel='precipitation (mm/day)',
             figsize=(20, 8))
a = add_changepoints_to_plot(fig.gca(), m, forecast)
