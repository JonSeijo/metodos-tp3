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
df_cancelaciones_clima_semana = pd.read_csv('datos/cancelaciones_semana_clima.csv')
df_cancelaciones_clima = pd.read_csv('datos/cancelaciones_mes_clima-2000-2008.csv')

df_cancelaciones_clima_semana['valor']


def listar_meses():
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


"""
# SOLO PARA GRAFICAR:

espaciado = 24
enum = [x for x in range(12*6*4 + 1)]
labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(4)]

ax = df_cancelaciones_clima_semana['valor'].plot(title='Cancelaciones por clima', linestyle='--', marker='o')

ax.set_xlabel('Semana')
ax.set_ylabel('Cancelaciones por semana')

ax.set_xticks(enum[::espaciado])
ax.set_xticklabels(labels[::espaciado], rotation=75)

plt.show()
"""

def plotear_cancelaciones(color_in=violeta):
    espaciado = 24
    enum = [x for x in range(12*6*4 + 1)]
    labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(4)]

    df_cancelaciones_clima_semana['y'] = df_cancelaciones_clima_semana['valor']
    df_cancelaciones_clima_semana['x'] = range(len(labels))

    ax = df_cancelaciones_clima_semana['valor'].plot(title='Cancelaciones por clima', linestyle='--', marker='o', color=color_in)

    ax.set_xlabel('Semana')
    ax.set_ylabel('Cancelaciones por semana')

    ax.set_xticks(enum[::espaciado])
    ax.set_xticklabels(labels[::espaciado], rotation=45)

    return ax



def entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion):
    # http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    regr = linear_model.LinearRegression(fit_intercept=False)

    ## Entreno el modelo

    # Armo la matriz A de features
    df_entrenamiento = df[df['x'].isin(rango_entrenamiento)]

    A = armar_matriz_A(df_entrenamiento['x'])

    # 'Fiteo' los datos de entrenamiento
    regr.fit(A, df_entrenamiento['y'])

    df_entrenamiento['pred'] = regr.predict(A)

    ## Realizo predicciones

    # Armo la matriz A de features
    df_prediccion = df[df['x'].isin(rango_prediccion)]
    A = armar_matriz_A(df_prediccion['x'])

    # Predigo los datos de testeo
    df_prediccion['pred'] = regr.predict(A)

    return (df_entrenamiento, df_prediccion)


def calcularECM(df_prediccion):
    ## Calculo el Error Cuadrático Medio
    ECM = sum((df_prediccion['pred'] - df_prediccion['y'])**2) / len(df_prediccion['y'])
    return ECM


def sumar_year(k, cant):
    return k + 12*4*cant


def restar_year(k, cant):
    return k - 12*4*cant


def get_year(year):
    return year*12*4


def predecir_cancelaciones(k):
    # Entreno 3 years hacia atras
    rango_entrenamiento = list(range(restar_year(k, 3), k+1))
    # Entreno 1 years hacia delante
    rango_prediccion = list(range(k, sumar_year(k, 1) + 1))

    return entrenar_y_predecir_en_rangos(df_cancelaciones_clima_semana, rango_entrenamiento, rango_prediccion)


def armar_matriz_A(s):
    return np.array([
        [
            1,
            np.sin(0.7*t),
            np.cos(0.7*t),
            np.sin(0.08 * t),
            np.cos(0.08 * t),

        ] for t in s])


ax = plotear_cancelaciones(azul)

# Predigo a partir del year 5
df_entrenamiento, df_prediccion = predecir_cancelaciones(get_year(5))

# Grafico predicciones y aproximacino
sns.tsplot(ax=ax, time=df_entrenamiento['x'], data=df_entrenamiento['pred'], color='red', legend=True)
sns.tsplot(ax=ax, time=df_prediccion['x'], data=df_prediccion['pred'], color='green', legend=True)

ax.legend(["Datos", "Aproximación", "Prediccion"])

print("ECM: " + str(calcularECM(df_prediccion)))

plt.xlim((0,get_year(6) + 5))
plt.show()