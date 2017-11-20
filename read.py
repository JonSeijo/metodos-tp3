import pandas as pd
import numpy as np
import math
import scipy.optimize as optimization
import matplotlib.pyplot as plt
import glob
fields = ['Year', 'Month', 'DayofMonth', 'CancellationCode']

#path =r'C:\Users\tytalus\Desktop\metodos-tp3\data' # use your path
#allFiles = glob.glob(path + "/*.csv")
#df = pd.DataFrame()
#list_ = []
#for file_ in allFiles:
#    dfaux = pd.read_csv(file_,index_col=None, header=0, encoding = 'utf8', usecols=fields)
#    list_.append(dfaux)
#df = pd.concat(list_)

# read csv file
ano = '2009'
df = pd.read_csv('./data/' + ano + '.csv')
# filter columns this should be done when we open the file probably
#df = df.loc[:,['Year','Month','DayofMonth','CancellationCode']]
df = df.rename(columns={'DayofMonth': 'day'})
df = df.assign(Date=pd.to_datetime(df[['Year', 'Month', 'day']]))
df.set_index(df["Date"],inplace=True)
df['CancellationTotals'] = df['CancellationCode'].apply(lambda x: 1 if x!='NaN' else 0)
df['CancellationsByWeather'] = df['CancellationCode'].apply(lambda x: 1 if x=='B' else 0)
print(df)

#df['CancellationCode'] = df['CancellationCode'].str.replace(r'\D+', '').astype('int')
#df['Date'] = pd.to_datetime(df['Date']) - pd.to_timedelta(7, unit='d')
#df = df.groupby(['Year', pd.Grouper(key='Date', freq='W-MON')])['CancellationsByWeather','CancellationTotals'].sum().reset_index().sort_values('Date')
grouped = (df.groupby('Year').apply(lambda g: g.set_index('Date')[['CancellationsByWeather', 'CancellationTotals']].resample('W', how='sum')).unstack(level=0).fillna(0))
df = grouped
df['CancellationsPercentage'] = df['CancellationsByWeather'] / df['CancellationTotals']
df = df.loc[:,['Date','CancellationsPercentage']]
df = df.rename(columns={'CancellationsPercentage': 'valor'})

df.to_csv('cancelaciones-semana-porcentaje-' + ano + '.csv')


#mapping = {'B': 1, 'test': 2}
#df.replace({'CancellationCode': mapping})

#df['CancellationCode'].resample('W', how='sum')


# pd.to_datetime(df)
#print(df)
# insert column to calculate the difference between times
'''
df.insert(2,'wasDelayed',df['CRSArrTime'])
print(df.head())
# calculate the difference 
df[['wasDelayed']].sub(df['ArrTime'], axis=0)
# transform difference to 0 (not delayed) or 1 (delayed) 
df['wasDelayed'] = df['wasDelayed'].map(lambda x: 0 if x >= 0 else 1)
# sum the amount of delayed fligths per month\
df.groupby('Month').agg({'wasDelayed' : np.sum})
#with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
print(df['wasDelayed'])
#for delayed in df.wasDelayed:
#    if(delayed==0): print('puto')
'''