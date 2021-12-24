import pandas as pd

prices = [3869.47, 7188.46, 22203.31, 29391.78, 33269.24, 49976.65, 59218.56, 40734.22]
s = pd.Series(prices)

print(s.describe())
print(s[6])

data = {'date': ['2017-06-10', '2018-06-11', '2019-06-12', '2020-06-13'],
        'prices': [3869.47, 7188.46, 22203.31, 29391.78]}
df = pd.DataFrame(data)
print(df)

data1 = pd.read_html('https://en.wikipedia.org/wiki/list_of_S%26P_500_companies')
df = data1[0]
print(df)

df = df[['Symbol', 'Security']]
print(df)

df.info()

