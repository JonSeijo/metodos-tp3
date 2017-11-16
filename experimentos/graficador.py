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


def listar_meses():
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Levanto los datos

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
df_delay_clima = pd.read_csv('datos/delays_mes_clima.csv')

df_cancelaciones_general = pd.read_csv('datos/cancelados_semana_general.csv')
df_cancelaciones_general_dest_atlanta = pd.read_csv('datos/cancelados_semana_general_dest_atlanta.csv')
df_cancelaciones_general_origen_atlanta = pd.read_csv('datos/cancelados_semana_general_origen_atlanta.csv')

df_cancelaciones_atlanta = pd.read_csv('datos/cancelados_destino_atlanta.csv')
df_cancelaciones_miami = pd.read_csv('datos/cancelados_destino_miami.csv')
df_cancelaciones_clima_atlanta = pd.read_csv('datos/cancelados_clima_destino_atlanta.csv')
df_cancelaciones_clima_miami = pd.read_csv('datos/cancelados_clima_destino_miami.csv')

df_cancelaciones_orig_miami = pd.read_csv('datos/cancelados_origen_miami.csv')
df_cancelaciones_clima_orig_miami = pd.read_csv('datos/cancelados_clima_origen_miami.csv')

df_delay_clima_orig_miami = pd.read_csv('datos/delay_clima_origen_miami.csv')
df_minutos_delay_clima_orig_miami = pd.read_csv('datos/minutos_delay_clima_origen_miami.csv')

df_cancelaciones_clima_semana = pd.read_csv('datos/cancelaciones_semana_clima.csv')
df_cancelaciones_clima = pd.read_csv('datos/cancelaciones_mes_clima-2000-2008.csv')


espaciado = 24
rotacion_xaxis = 50
enum = [x for x in range(12*6*4 + 1)]
labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(4)]


def ajustar_ax(ax, xlabel='Semana', ylabel='Eventos por semana', legend=['Cancelaciones']):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(enum[::espaciado])
    ax.set_xticklabels(labels[::espaciado], rotation=rotacion_xaxis)
    ax.legend(legend)



def plot_delay_cancelaciones_miami():
    ax = df_delay_clima_orig_miami['valor'].plot(title='Miami - Delays vs Cancelaciones - Clima', linestyle='--', marker='o')
    df_cancelaciones_clima_orig_miami['valor'].plot(ax=ax, linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Delay Miami - Clima', 'Cancelaciones Miami - Clima'])
    plt.show()


# DELAYS MINUTOS CLIMA MIAMI
def plot_delay_clima_minutos_miami():
    ax = df_minutos_delay_clima_orig_miami['valor'].plot(title='Miami - Delays por clima en minutos', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Minutos de delay por clima', legend=['Delay Miami - Clima'])
    plt.show()


# CANCELACIONES GENERAL
def plot_cancelados_gral():
    ax = df_cancelaciones_general['valor'].plot(title='Cancelaciones - general', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones por semana'])
    plt.show()



# CANCELACIONES GENERAL - DESTINO ATLANTA
# 2005: Tormenta de invierno de Georgia     https://www.weather.gov/ffc/istorm13005
def plot_cancelados_gral_dest_atlanta():
    ax = df_cancelaciones_general_dest_atlanta['valor'].plot(title='Cancelaciones - Aeropuerto de Atlanta', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones por semana'])
    plt.show()


# CANCELACIONES GENERAL - ORIGEN ATLANTA
# 2005: Tormenta de invierno de Georgia     https://www.weather.gov/ffc/istorm13005
def plot_cancelados_gral_origen_atlanta():
    ax = df_cancelaciones_general_origen_atlanta['valor'].plot(title='Cancelaciones - Aeropuerto de Atlanta', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones por semana'])
    plt.show()


# -----------------------------------------------------
# CUADRADOS MINIMOS

def preplot_cuadminimos(df, ylabel='Cancelaciones por semana', color=azul):
    df['y'] = df['valor']
    df['x'] = range(len(labels))
    ax = df['valor'].plot(title='Cancelaciones por clima', linestyle='--', marker='o', color=color)
    ajustar_ax(ax, xlabel='Semana', ylabel=ylabel)
    return ax


def entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion):
    # http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    regr = linear_model.LinearRegression(fit_intercept=False)

    # Armo la matriz A de features
    df_entrenamiento = df[df['x'].isin(rango_entrenamiento)]

    A = armar_matriz_A(df_entrenamiento['x'])
    # 'Fiteo' los datos de entrenamiento
    regr.fit(A, df_entrenamiento['y'])

    ## Realizo predicciones
    df_entrenamiento['pred'] = regr.predict(A)

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


def predecir_cancelaciones(df, k):
    # Entreno 3 years hacia atras
    rango_entrenamiento = list(range(restar_year(k, 3), k+1))
    # Entreno 1 years hacia delante
    rango_prediccion = list(range(k, sumar_year(k, 1) + 1))

    return entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion)


def armar_matriz_A(s):
    return np.array([
        [
            1,
            np.sin(0.7*t),
            np.cos(0.7*t),
            np.sin(0.08 * t),
            np.cos(0.08 * t),
        ] for t in s])



def cuadrados_minimos(df, ylabel='Cancelaciones por semana'):
    ax = preplot_cuadminimos(df, ylabel=ylabel, color=azul)
    # Predigo a partir del year 5
    df_entrenamiento, df_prediccion = predecir_cancelaciones(df, get_year(5))

    # Grafico predicciones y aproximacino
    sns.tsplot(ax=ax, time=df_entrenamiento['x'], data=df_entrenamiento['pred'], color='red', legend=True)
    sns.tsplot(ax=ax, time=df_prediccion['x'], data=df_prediccion['pred'], color='green', legend=True)

    ax.legend(["Datos", "Aproximación", "Prediccion"])

    print("ECM: " + str(calcularECM(df_prediccion)))

    plt.xlim((0, get_year(6) + 5))
    plt.show()



# plot_delay_cancelaciones_miami()
# plot_delay_clima_minutos_miami()
# plot_cancelados_gral()
# plot_cancelados_gral_dest_atlanta()
# plot_cancelados_gral_origen_atlanta()

cuadrados_minimos(df_cancelaciones_general_origen_atlanta)