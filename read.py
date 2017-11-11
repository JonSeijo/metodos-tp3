import pandas as pd
import numpy as np
import math
import scipy.optimize as optimization
import matplotlib.pyplot as plt

# read csv file
df = pd.read_csv('./data/1987.csv')
# filter columns this should be done when we open the file probably
df = df.loc[:,['Year','Month','ArrTime','CRSArrTime']]
# insert column to calculate the difference between times
df.insert(2,'wasDelayed',df['CRSArrTime'])
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