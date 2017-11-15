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


# Levanto los datos

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
df_delay_clima = pd.read_csv('datos/delays_mes_clima.csv')

df_cancelaciones_atlanta = pd.read_csv('datos/cancelados_destino_atlanta.csv')
df_cancelaciones_miami = pd.read_csv('datos/cancelados_destino_miami.csv')
df_cancelaciones_clima_atlanta = pd.read_csv('datos/cancelados_clima_destino_atlanta.csv')
df_cancelaciones_clima_miami = pd.read_csv('datos/cancelados_clima_destino_miami.csv')

df_cancelaciones_orig_miami = pd.read_csv('datos/cancelados_origen_miami.csv')
df_cancelaciones_clima_orig_miami = pd.read_csv('datos/cancelados_clima_origen_miami.csv')

df_delay_clima_orig_miami = pd.read_csv('datos/delay_clima_origen_miami.csv')

df_cancelaciones_clima_semana = pd.read_csv('datos/cancelaciones_semana_clima.csv')
df_cancelaciones_clima = pd.read_csv('datos/cancelaciones_mes_clima-2000-2008.csv')


def listar_meses():
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def plot_delay_cancelaciones_miami():
    espaciado = 24
    enum = [x for x in range(12*6*4 + 1)]
    labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(4)]

    ax = df_delay_clima_orig_miami['valor'].plot(title='Miami - Delays vs Cancelaciones - Clima', linestyle='--', marker='o')
    df_cancelaciones_clima_orig_miami['valor'].plot(ax=ax, linestyle='--', marker='o')

    ax.set_xlabel('Semana')
    ax.set_ylabel('Eventos por semana')

    ax.set_xticks(enum[::espaciado])
    ax.set_xticklabels(labels[::espaciado], rotation=45)

    ax.legend(['Delay Miami - Clima', 'Cancelaciones Miami - Clima'])

    # ax.set_xticklabels(list(df_dummy['test']))
    plt.show()













plot_delay_cancelaciones_miami()