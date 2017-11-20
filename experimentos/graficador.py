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
# df_delay_clima = pd.read_csv('datos/delays_mes_clima.csv')

# df_cancelaciones_general = pd.read_csv('datos/cancelados_semana_general.csv')
# df_cancelaciones_general_origen_atlanta = pd.read_csv('datos/cancelados_semana_general_origen_atlanta.csv')

# df_cancelaciones_atlanta = pd.read_csv('datos/cancelados_destino_atlanta.csv')
# df_cancelaciones_miami = pd.read_csv('datos/cancelados_destino_miami.csv')
# df_cancelaciones_clima_atlanta = pd.read_csv('datos/cancelados_clima_destino_atlanta.csv')
# df_cancelaciones_clima_miami = pd.read_csv('datos/cancelados_clima_destino_miami.csv')

# df_cancelaciones_clima_orig_miami = pd.read_csv('datos/cancelados_clima_origen_miami.csv')
# df_cancelaciones_clima_orig_miami_sinouts = pd.read_csv('datos/cancelados_clima_origen_miami_sinouts.csv')

# df_delay_clima_orig_miami = pd.read_csv('datos/delay_clima_origen_miami.csv')
# df_cancelaciones_origen_orlando = pd.read_csv('datos/cancelados_gral_origen_orlando.csv')

df_cancelaciones_origen_orlando_sin_outliers = pd.read_csv('datos/orlando_cancel_sin_outliers.csv')
df_cancelaciones_origen_miami_sin_outliers = pd.read_csv('datos/miami_cancel_sin_outliers.csv')

df_cancelaciones_origen_detroit = pd.read_csv('datos/cancelados_semana_origen_detroit.csv')
df_cancelaciones_origen_losangeles = pd.read_csv('datos/cancelados_semana_clima_losangeles.csv')
df_cancelaciones_clima_origen_orlando = pd.read_csv('datos/cancelados_semana_clima_orlando.csv')

# df_cancelados_semana_clima_deltaairlines = pd.read_csv('datos/cancelados_semana_clima_deltaairlines.csv')
# df_delays_semana_clima_deltaairlines = pd.read_csv('datos/delays_semana_clima_deltaairlines.csv')
# df_cancelados_semana_deltaairlines = pd.read_csv('datos/cancelados_semana_deltanairlines.csv')
# df_cancelados_semana_expressjet = pd.read_csv('datos/cancelados_semana_expressjet.csv')
# df_cancelados_semana_unitedairlines = pd.read_csv('datos/cancelados_semana_unitedairlines.csv')
# df_cancelados_semana_atlanta_unitedairlines = pd.read_csv('datos/cancelados_semana_atlanta_unitedairlines.csv')

# df_delays_semana_atlanta_unitedairlines = pd.read_csv('datos/delays_semana_atlanta_unitedairlines.csv')

df_delays_semana_losangeles_expressjet = pd.read_csv('datos/delays_semana_losangeles_expressjet.csv')
df_delays_semana_losangeles_unitedairlines = pd.read_csv('datos/delays_semana_losangeles_unitedairlines.csv')
df_delays_semana_losangeles_deltaairlines = pd.read_csv('datos/delays_semana_losangeles_deltaairlines.csv')
df_delays_semana_losangeles_americanairlines = pd.read_csv('datos/delays_semana_losangeles_americanairlines.csv')
df_delays_semana_losangeles_southwestairlines = pd.read_csv('datos/delays_semana_losangeles_southwestairlines.csv')


df_delays_semana_atlanta_unitedairlines = pd.read_csv('datos/delays_semana_atlanta_unitedairlines.csv')
df_delays_semana_atlanta_deltaairlines = pd.read_csv('datos/delays_semana_atlanta_deltaairlines.csv')
df_delays_semana_atlanta_americanairlines = pd.read_csv('datos/delays_semana_atlanta_americanairlines.csv')
df_delays_semana_atlanta_southwestairlines = pd.read_csv('datos/delays_semana_atlanta_southwestairlines.csv')



# df_delays_semana_expressjet = pd.read_csv('datos/delays_semana_expressjet.csv')

df_cancelados_semana_americanairlines = pd.read_csv('datos/cancelados_semana_americanairlines.csv')
# df_cancelados_semana_americanairlines_sinoutliers = pd.read_csv('datos/cancelados_semana_americanairlines_sinoutliers.csv')
# df_delays_semana_americanairlines = pd.read_csv('datos/delays_semana_americanairlines.csv')

rotacion_xaxis = 70
rotacion_xaxis_years = 0

pormes = 4
espaciado = 6*pormes
espaciado_years = 12*pormes

enum = [x for x in range(12*6*pormes + 1)]

labels = [str(year) + " - " + str(mes) for year in range(2003, 2009) for mes in listar_meses() for semana in range(pormes)]
labels_years = [" "*24 + str(year) for year in range(2003, 2009) for mes in listar_meses() for semana in range(pormes)]

# print(len(labels))

def ajustar_ax(ax, xlabel='Semana', ylabel='Eventos por semana', legend=['Cancelaciones']):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    #   Labels del estilo  "Mes - año"
    # ax.set_xticks(enum[::espaciado])
    # ax.set_xticklabels(labels[::espaciado], rotation=rotacion_xaxis)

    # #   Labels del estilo  "Año"
    ax.set_xticks(enum[::espaciado_years])
    ax.set_xticklabels(labels_years[::espaciado_years], rotation=rotacion_xaxis_years)


    ax.legend(legend)



def plot_delay_cancelaciones_miami():
    ax = df_delay_clima_orig_miami['valor'].plot(title='Miami - Delays vs Cancelaciones - Clima', linestyle='--', marker='o')
    df_cancelaciones_clima_orig_miami['valor'].plot(ax=ax, linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Delay Miami - Clima', 'Cancelaciones Miami - Clima'])
    plt.show()

# Miami - cancelaciones clima
def plot_cancelaciones_clima_miami():
    ax = df_cancelaciones_clima_orig_miami['valor'].plot(title='Cancelaciones por clima - Miami', linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Miami - Clima'])
    plt.show()

#Miami vs Orlando
def plot_miami_vs_orlando_cancelaciones_origen():
    ax = df_cancelaciones_origen_orlando['valor'].plot(title='Miami vs. Orlando, cancelaciones por clima', linestyle='--', marker='o')
    df_cancelaciones_clima_orig_miami['valor'].plot(ax=ax, linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Orlando - Clima', 'Cancelaciones Miami - Clima'])
    plt.show()

#Miami vs Orlando no outliers
def plot_miami_vs_orlando_cancelaciones_origen():
    ax = df_cancelaciones_origen_orlando_sin_outliers['valor'].plot(title='Miami vs. Orlando, cancelaciones por clima (sin outliers)', linestyle='--', marker='o')
    df_cancelaciones_origen_miami_sin_outliers['valor'].plot(ax=ax, linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Orlando - Clima', 'Cancelaciones Miami - Clima'])
    plt.show()


# Cancelaciones Orlando - clima
def plot_cancelaciones_clima_orlando():
    ax = df_cancelaciones_clima_origen_orlando['valor'].plot(title='Cancelaciones por clima - Orlando', linestyle='--', marker='o')
    ajustar_ax(ax, legend=['Cancelaciones Clima - Orlando'])
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


# CANCELACIONES CLIMA GENERAL
def plot_cancelados_clima_gral():
    ax = df_cancelaciones_clima_semana['valor'].plot(title='Cancelaciones Clima - General', linestyle='--', marker='o')
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

# Cancelaciones general - origen Orlando
def plot_cancelados_gral_origen_orlando():
    ax = df_cancelaciones_origen_orlando['valor'].plot(title='Cancelaciones - Aeropuerto de Orlando', linestyle='--', marker='o')
    ajustar_ax(ax, ylabel='Cantidad de cancelaciones', legend=['Cancelaciones Orlando - Clima'])
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
    return k + 12*pormes*cant


def restar_year(k, cant):
    return k - 12*pormes*cant


def get_year(year):
    return year*pormes*12


def predecir_cancelaciones(df, k):
    # Entreno 3 years hacia atras
    rango_entrenamiento = list(range(restar_year(k, 3), k+1))
    # Entreno 1 years hacia delante
    rango_prediccion = list(range(k, sumar_year(k, 1) + 1))

    return entrenar_y_predecir_en_rangos(df, rango_entrenamiento, rango_prediccion)


"""
Para df_cancelaciones_general_origen_atlanta

ECM: 11841.8727878
1,
t,
np.sin(np.pi/(12.0*4.0)*t),
np.cos(np.pi/(12.0*4.0)*t),
np.sin(np.pi/(6.0*4.0) * t),
np.cos(np.pi/(6.0*4.0) * t),
np.sin(np.pi/(3.0*4.0) * t),
np.cos(np.pi/(3.0*4.0) * t),
"""



"""
Para df_cancelaciones_clima_semana

1,
np.cos(np.pi/(12.0*4.0)*t)**8,
np.sin(np.pi/(6.0*4.0) * t),
np.sin(np.pi/(3.0*4.0) * t),
"""


"""
Para delays_expressjet
1
np.cos(np.pi/(48.0*4.0) * t ),
np.cos(np.pi/(12.0*4.0) * t ),
np.cos(np.pi/(6.0*4.0) * t ),
"""

def armar_matriz_A(s):
    return np.array([
        [
            1,
            # t,
            # np.log(t+1),
            # t**2,
            # np.cos(np.pi/(12.0*4.0)*t)**8,
            # np.sin(np.pi/(6.0*4.0) * t),
            # np.sin(np.pi/(3.0*4.0) * t),

            # np.cos(np.pi/(48.0*4.0) * t ),
            # np.cos(np.pi/(12.0*4.0) * t ),

            # 1570
            # np.log(t+1),
            # np.cos(np.pi/(12.0*4.0) * t ),
            # np.cos(np.pi/(3.0*4.0) * t ),

            # t,
            # np.log(t+1),


            # UNITED AIRLINES - Mejor en gral
            # np.cos(np.pi/(48.0*4.0) * t ),
            # np.cos(np.pi/(12.0*4.0) * t ),
            # np.cos(np.pi/(6.0*4.0) * t ),


            # DELTA AIRLINES - Bastante buena
            # AMERICAN AIRLINES - Mejor en gral
            np.cos(np.pi/(48.0*4.0) * t ),
            np.cos(np.pi/(12.0*4.0) * t ),
            np.cos(np.pi/(6.0*4.0) * t ),
            np.cos(np.pi/(3.0*4.0) * t ),



            # 2286
            # np.cos(np.pi/(24.0*4.0) * t ),
            # np.cos(np.pi/(6.0*4.0) * t ),
            # np.cos(np.pi/(3.0*4.0) * t ),

            # 2422
            # np.cos(np.pi/(24.0*4.0) * t ),
            # np.cos(np.pi/(12.0*4.0) * t ),
            # np.cos(np.pi/(6.0*4.0) * t ),
            # np.cos(np.pi/(3.0*4.0) * t ),

            # 1373
            # np.cos(np.pi/(96.0*4.0) * t ),
            # np.cos(np.pi/(6.0*4.0) * t ),
            # np.cos(np.pi/(3.0*4.0) * t ),

            # 2105
            # np.cos(np.pi/(48.0*4.0) * t ),
            # np.cos(np.pi/(6.0*4.0) * t ),
            # np.cos(np.pi/(3.0*4.0) * t ),



        ] for t in s])


def cuadrados_minimos(df, titulo='Cancelaciones por clima', ylabel='Cancelaciones por semana'):
    ecmtotal = []

    for year_inicial in range(3,6):
        ax = preplot_cuadminimos(df, title=titulo, ylabel=ylabel, color=azul)
        # Predigo a partir del year 5
        # df_entrenamiento, df_prediccion = predecir_cancelaciones(df, get_year(5))
        df_entrenamiento, df_prediccion = predecir_cancelaciones(df, get_year(year_inicial))

        # Grafico predicciones y aproximacino
        sns.tsplot(ax=ax, time=df_entrenamiento['x'], data=df_entrenamiento['pred'], color='red', legend=True)
        sns.tsplot(ax=ax, time=df_prediccion['x'], data=df_prediccion['pred'], color='green', legend=True)

        ax.legend(["Datos", "Aproximación", "Prediccion"])

        ecmtotal.append(calcularECM(df_prediccion))
        print("ECM: " + str(calcularECM(df_prediccion)))

        plt.xlim((0, get_year(6)))
        plt.show()

    print("ECM TOTAL:", sum(ecmtotal)/len(ecmtotal))
    print("\n")


# cuadrados_minimos(df_cancelaciones_clima_orig_miami, titulo='Cancelaciones por clima - Miami')
# cuadrados_minimos(df_cancelaciones_clima_orig_miami_sinouts, titulo='Cancelaciones por clima - Miami (Sin outliers)')
# cuadrados_minimos(df_cancelaciones_origen_losangeles, titulo='Cancelaciones por clima - Los Ángeles')
# cuadrados_minimos(df_cancelaciones_clima_origen_orlando, titulo='Cancelaciones por clima - Orlando')


# cuadrados_minimos(df_cancelados_semana_unitedairlines, titulo='Cancelaciones - United Airlines')
# cuadrados_minimos(df_cancelados_semana_atlanta_unitedairlines, titulo='Cancelaciones - Atlanta - United Airlines')
# cuadrados_minimos(df_delays_semana_atlanta_unitedairlines, titulo='Retrasos - Atlanta - United Airlines', ylabel='Retrasos por semana')
# cuadrados_minimos(df_cancelados_semana_expressjet, titulo='Cancelaciones - Express Jet')
# cuadrados_minimos(df_cancelados_semana_deltaairlines, titulo='Cancelaciones - Delta Airlines')
# cuadrados_minimos(df_cancelados_semana_americanairlines, titulo='Cancelaciones - American Airlines')

# cuadrados_minimos(df_delays_semana_atlanta_deltaairlines, titulo='Retrasos - Atlanta - Delta Airlines', ylabel='Retrasos por semana')
# cuadrados_minimos(df_delays_semana_atlanta_southwestairlines, titulo='Retrasos - Atlanta - SouthWest Airlines', ylabel='Retrasos por semana')



# cuadrados_minimos(df_delays_semana_losangeles_unitedairlines, titulo='Retrasos - Los Angeles - United Airlines', ylabel='Retrasos por semana')
# cuadrados_minimos(df_delays_semana_losangeles_deltaairlines, titulo='Retrasos - Los Angeles - Delta Airlines', ylabel='Retrasos por semana')
cuadrados_minimos(df_delays_semana_losangeles_americanairlines, titulo='Retrasos - Los Angeles - American Airlines', ylabel='Retrasos por semana')
# cuadrados_minimos(df_delays_semana_losangeles_southwestairlines, titulo='Retrasos - Los Angeles - SouthWest Airlines', ylabel='Retrasos por semana')

# cuadrados_minimos(df_delays_semana_atlanta_unitedairlines, titulo='Retrasos - Atlanta - United Airlines', ylabel='Retrasos por semana')
cuadrados_minimos(df_delays_semana_atlanta_americanairlines, titulo='Retrasos - Atlanta - American Airlines', ylabel='Retrasos por semana')

