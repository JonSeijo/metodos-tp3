# Imports de clase de Francisco

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

# Levanto datos
df_cancelaciones_general = pd.read_csv('datos/cancelados_semana_general.csv')

df_cancelaciones_atlanta = pd.read_csv('datos/cancelados_destino_atlanta.csv')
df_cancelaciones_miami = pd.read_csv('datos/cancelados_destino_miami.csv')
df_cancelaciones_origen_detroit = pd.read_csv('datos/cancelados_semana_origen_detroit.csv')
df_cancelaciones_origen_losangeles = pd.read_csv('datos/cancelados_semana_clima_losangeles.csv')

# -----------------------------------------------------------------

rotacion_xaxis = 70
rotacion_xaxis_years = 0

pormes = 4
espaciado = 6*pormes
espaciado_years = 12*pormes

# Armo los labels del eje x para los graficos
enum = [x for x in range(12*6*pormes + 1)]
labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(pormes)]
labels_years = [" "*24 + str(year) for year in range(2003, 2009) for mes in listar_meses() for semana in range(pormes)]

# -----------------------------------------------------------------

def ajustar_ax(ax, xlabel='Semana', ylabel='Eventos por semana', legend=['Cancelaciones']):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    #   Labels del estilo  "Mes - Año"
    # ax.set_xticks(enum[::espaciado])
    # ax.set_xticklabels(labels[::espaciado], rotation=rotacion_xaxis)

    # #   Labels del estilo  "Año"
    ax.set_xticks(enum[::espaciado_years])
    ax.set_xticklabels(labels_years[::espaciado_years], rotation=rotacion_xaxis_years)

    ax.legend(legend)



# CANCELACIONES GENERAL
def plot_cancelados_gral():
    ax = df_cancelaciones_general['valor'].plot(title='Cancelaciones - general', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones por semana'])
    plt.show()


# CANCELACIONES CLIMA GENERAL
def plot_cancelados_clima_gral():
    ax = df_cancelaciones_clima_semana['valor'].plot(title='Cancelaciones Clima - General', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones por semana'])
    plt.show()


#Miami vs Orlando
def plot_miami_vs_orlando_cancelaciones_origen():
    ax = df_cancelaciones_origen_orlando['valor'].plot(title='Miami vs. Orlando, cancelaciones por clima', linestyle='--', marker='o')
    df_cancelaciones_clima_orig_miami['valor'].plot(ax=ax, linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Orlando - Clima', 'Cancelaciones Miami - Clima'])
    plt.show()


# Cancelaciones Orlando - clima
def plot_cancelaciones_clima_orlando():
    ax = df_cancelaciones_clima_origen_orlando['valor'].plot(title='Cancelaciones por clima - Orlando', linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Clima - Orlando'])
    plt.show()



# -----------------------------------------------------
# CUADRADOS MINIMOS

def preplot_cuadminimos(df, title='Cancelaciones por Clima',ylabel='Cancelaciones por semana', color=azul):
    df['y'] = df['valor']
    df['x'] = range(len(labels))
    ax = df['valor'].plot(title=title, linestyle='--', marker='o', color=color)
    ajustar_ax(ax, xlabel='Semana', ylabel=ylabel)
    return ax


def entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion):
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
    return sum((df_prediccion['pred'] - df_prediccion['y'])**2) / len(df_prediccion['y'])


def sumar_year(k, cant):
    return k + 12*pormes*cant


def restar_year(k, cant):
    return k - 12*pormes*cant


def get_year(year):
    return year*pormes*12


def predecir_cancelaciones(df, k):
    # Entreno 3 años hacia atras
    rango_entrenamiento = list(range(restar_year(k, 3), k+1))
    # Entreno 1 año hacia delante
    rango_prediccion = list(range(k, sumar_year(k, 1) + 1))

    return entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion)



def armar_matriz_A(s):
    return np.array([
        [
            1,
            t,
            np.cos(np.pi/(12.0*4.0)* t),
            np.cos(np.pi/(6.0*4.0) * t),
            np.cos(np.pi/(3.0*4.0) * t)
        ] for t in s])


def cuadrados_minimos(df, titulo='Cancelaciones por clima', ylabel='Cancelaciones por semana'):
    ecmtotal = []

    for year_inicial in range(3,6):
        ax = preplot_cuadminimos(df, title=titulo, ylabel=ylabel, color=azul)

        # Predigo a partir de year_inicial
        df_entrenamiento, df_prediccion = predecir_cancelaciones(df, get_year(year_inicial))

        # Grafico predicciones y aproximacinon
        sns.tsplot(ax=ax, time=df_entrenamiento['x'], data=df_entrenamiento['pred'], color='red', legend=True)
        sns.tsplot(ax=ax, time=df_prediccion['x'], data=df_prediccion['pred'], color='green', legend=True)

        ax.legend(["Datos", "Aproximación", "Prediccion"])

        ecmtotal.append(calcularECM(df_prediccion))
        print("ECM: " + str(calcularECM(df_prediccion)))

        plt.xlim((0, get_year(6)))
        plt.show()

    print("ECM TOTAL:", sum(ecmtotal)/len(ecmtotal))
    print("\n")

# ----------------------------------------------------------

cuadrados_minimos(df_cancelaciones_general, titulo='Cancelaciones - General', ylabel='Cancelaciones por semana')
