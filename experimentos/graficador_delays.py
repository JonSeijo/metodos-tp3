import pandas as pd                  # Para trabajar con datos
import numpy as np                   # Para cosas de álgebra lineal
import matplotlib.pyplot as plt      # Para gráficos
import seaborn as sns                # Para gráficos lindos :^)
sns.set_style("darkgrid")
from sklearn import linear_model     # Para CML
import random

import warnings
warnings.filterwarnings('ignore')  # Cállese, hombre horrible!

# Levanto los datos

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
df_delay_clima = pd.read_csv('delays_mes_clima.csv')



rango_completo = pd.DatetimeIndex(start='2000-01-01',end='2009-01-01' , freq='M')
rango_temporal = pd.DatetimeIndex(start='2003-01-01',end='2009-01-01' , freq='M')
serie = pd.Series(np.array(df_delay_clima['WeatherDelay'][len(rango_completo) - len(rango_temporal):]), index=rango_temporal)

ax = serie.plot(title='Delays por clima', linestyle='--', marker='o')
ax.set_xlabel('Fecha')
ax.set_ylabel('Cantidad de Delays')
plt.show()