import yfinance as yf
import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')
price = data.history(period='1y')

x = price['Close'].pct_change()

x.plot()

plt.savefig('plot.png')

data = yf.Ticker('TSLA')
price = data.history(period='1y')

x = price['Close'].pct_change()

x.plot(kind='hist')

plt.savefig('plot.png')

data = yf.download("AAPL MSFT TSLA", start='2021-01-01') 

x = data['Close'].pct_change()
(x + 1).cumprod().plot()

plt.savefig('plot.png')


import statsmodels.api as sm

data = yf.download("FB AMZN AAPL NFLX GOOG", start='2020-01-01') 
x = data['Close'].pct_change()
corr = x.corr()

sm.graphics.plot_corr(corr, xnames=list(x.columns))

plt.savefig('plot.png')


stocks = ['AAPL', 'AMZN', 'MSFT', 'TSLA']
weights = [0.3, 0.2, 0.4, 0.1]

data = yf.download(stocks, start='2021-01-01')

#daily returns
x = data['Close'].pct_change()

#portfolio return
ret = (x * weights).sum(axis = 1)

#total cumulative returns for our portfolio
cumulative = (ret + 1).cumprod() 

cumulative.plot()

plt.savefig('plot.png')

import numpy as np

stocks = ['AAPL', 'AMZN', 'MSFT', 'TSLA']
weights = [0.3, 0.2, 0.4, 0.1]

data = yf.download(stocks, start='2021-01-01')

#daily returns
x = data['Close'].pct_change()

#portfolio return
ret = (x * weights).sum(axis = 1)

annual_std = np.std(ret) * np.sqrt(252)
print(annual_std)