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
#df_cancelaciones_clima = pd.read_csv('datos/cancelaciones_mes_clima-2000-2008.csv')
#df_cancelaciones_clima = pd.read_csv('datos/canc_por_mes-origen-Orlando-2003-2008.csv')
df_cancelaciones_clima = pd.read_csv('datos/canc_por_mes-origen-Detroit-2003-2008.csv')

def plotear_cancelaciones(color_in=violeta):
    rango_completo = pd.DatetimeIndex(start='2003-01-01',end='2009-01-01' , freq='M')
    rango_temporal = pd.DatetimeIndex(start='2003-01-01',end='2009-01-01' , freq='M')
    serie = pd.Series(np.array(df_cancelaciones_clima['valor'][len(rango_completo) - len(rango_temporal):]), index=rango_temporal)

    df_cancelaciones_clima['Meses'] = range(len(rango_completo))
    df_cancelaciones_clima['y'] = df_cancelaciones_clima['valor']

    ax = df_cancelaciones_clima['y'].plot(x=serie, title='Cancelaciones por clima desde 2003 Detroit', linestyle='--', marker='o', color=color_in)
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Cantidad de cancelaciones')

    return ax


def armar_matriz_A(s):
    return np.array([
        [
            1,
            t,
            t**2,
            abs((np.cos(np.pi/12.0 *(t)))**600),
            abs((np.sin(np.pi/12.0 *(t)))**600),
            #np.cos(t),
            #np.sin(t),
            #300*np.cos(t),
            #300*np.sin(t),
            #np.cos(np.pi *t),
            #np.sin(np.pi *t),
            np.cos(np.pi/12.0 *t)**50,
            np.sin(np.pi/12.0 *t)**50,
            #abs((np.cos(np.pi/12.0 *(t-3)))**4),
            #abs((np.sin(np.pi/12.0 *(t-3)))**4),
            #abs((np.cos(np.pi/6.0 *(t-3)))**4),
            #abs((np.sin(np.pi/6.0 *(t-3))))**4,
            #np.e**(-(((t-20)*4)**2))
            np.sin(t)*np.cos(t),
            #np.e

        ] for t in s])

def entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion):
    # http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    regr = linear_model.LinearRegression(fit_intercept=False)

    ## Entreno el modelo

    # Armo la matriz A de features
    df_entrenamiento = df[df['Meses'].isin(rango_entrenamiento)]

    A = armar_matriz_A(df_entrenamiento['Meses'])

    # 'Fiteo' los datos de entrenamiento
    regr.fit(A, df_entrenamiento['y'])

    df_entrenamiento['pred'] = regr.predict(A)

    ## Realizo predicciones

    # Armo la matriz A de features
    df_prediccion = df[df['Meses'].isin(rango_prediccion)]
    A = armar_matriz_A(df_prediccion['Meses'])

    # Predigo los datos de testeo
    df_prediccion['pred'] = regr.predict(A)

    return (df_entrenamiento, df_prediccion)


def calcularECM(df_prediccion):
    ## Calculo el Error Cuadrático Medio
    ECM = sum((df_prediccion['pred'] - df_prediccion['y'])**2) / len(df_prediccion['y'])
    return ECM


def predecir_cancelaciones(k):
    rango_entrenamiento = list(range(k-12*4,k+1))
    rango_prediccion_nogranular = list(range(k,k+12*1 + 1))

    # 3 veces mayor granularidad, NO FUNCA
    # print("ESTOY CAMBIANDO LA GRANULARIDAD OJO CON EL CALCULO DEL ERROR CUADRATICO MEDIO")
    # rango_prediccion = [newx for x in rango_prediccion_nogranular for newx in [x, x + 1/3.0, x +2/3.0] ]

    return entrenar_y_predecir_en_rangos(df_cancelaciones_clima, rango_entrenamiento, rango_prediccion_nogranular)


ax = plotear_cancelaciones(azul)

df_entrenamiento, df_prediccion = predecir_cancelaciones(12*3)

# Grafico predicciones y aproximacino
sns.tsplot(ax=ax, time=df_entrenamiento['Meses'], data=df_entrenamiento['pred'], color='red', legend=True)
sns.tsplot(ax=ax, time=df_prediccion['Meses'], data=df_prediccion['pred'], color='green', legend=True)

ax.legend(["Datos", "Aproximación", "Prediccion"])

print("ECM: " + str(calcularECM(df_prediccion)))

plt.xlim((-5,12*6 + 5))
plt.show()