import pandas as pd                  # Para trabajar con datos
import numpy as np                   # Para cosas de álgebra lineal
import matplotlib.pyplot as plt      # Para gráficos
import seaborn as sns                # Para gráficos lindos :^)
sns.set_style("darkgrid")
from sklearn import linear_model     # Para CML
import random

import warnings
warnings.filterwarnings('ignore')  # Cállese, hombre horrible!

verde = '#55A868'
rojo = '#C44E52'
azul = '#4C72B0'
amarillo = '#EAEA25'
violeta = '#591463'

T_DELAY = 0
T_CANCEL = 1

# Levanto los datos
df_delay_clima = pd.read_csv('delays_mes_clima.csv')
df_cancelaciones_clima = pd.read_csv('cancelaciones_mes_clima-2000-2008.csv')

TIPO = T_DELAY

rango_completo = pd.DatetimeIndex(start='2000-01-01',end='2009-01-01' , freq='M')
rango_temporal = pd.DatetimeIndex(start='2003-01-01',end='2009-01-01' , freq='M')

datos = [
    ("Delays", df_delay_clima['WeatherDelay'], azul),
    ("Cancelaciones", df_cancelaciones_clima['Cancelaciones'], rojo)
]

# -------------------------------------
# SOLO DELAYS/CANCELS
# serie = pd.Series(np.array(datos[TIPO][1][len(rango_completo) - len(rango_temporal):]), index=rango_temporal)
# plot_datos = serie.plot(title=datos[TIPO][0] + ' por clima',
#     linestyle='--', marker='o', color=datos[TIPO][2])
# plot_datos.set_ylabel('Cantidad de ' + datos[TIPO][0])
# plot_datos.set_xlabel('Fecha')

# -------------------------------------
# LOS DOS JUNTOS
serie = pd.Series(np.array(datos[T_DELAY][1][len(rango_completo) - len(rango_temporal):]), index=rango_temporal)
plot_datos = serie.plot(title='Eventualidades por clima',
    linestyle='--', marker='o', color=datos[T_DELAY][2])

serie2 = pd.Series(np.array(datos[T_CANCEL][1][len(rango_completo) - len(rango_temporal):]), index=rango_temporal)
serie2.plot(ax=plot_datos, linestyle='--', marker='o', color=datos[T_CANCEL][2])

plot_datos.set_ylabel('Cantidad de eventualidades')
plot_datos.set_xlabel('Fecha')
plot_datos.legend(['Delays', 'Cancelaciones'])
# -----------------------------------------



plt.show()