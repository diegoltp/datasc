#manejo de base de datos y funciones estadisticas
import pandas as pd
import numpy as np
#Generar graficas y estilos de graficos.
import matplotlib.pyplot as plt
import seaborn as sns

# Inspeccion, NAN, recod DF
def reemplazar_noNaN(data:pd, simbolo:str, dev_listas=False):
    ''' 
    Cuenta valores perdidos con formato distintos a NaN, luego los reemplaza por np.nan
    si dev_listas=True devuelve ambas listas con los index
    data [pd.Series]: Base de datos
    simbolo[str]: Caracter o cadena de caracteres considerado como NaN
    '''
    col_con_simbolo=[]
    col_sin_simbolo=[]
    print(f'-------Contando {simbolo} -----------------')
    for index, row in data.iteritems():
        try:
            data[index].loc[data[index]==simbolo].value_counts().index[0]
            count = data[index].loc[data[index]==simbolo].value_counts()[0]
            print(f'{index} : {count}')
            col_con_simbolo.append(index)
        except:
            col_sin_simbolo.append(index)
    print(f'-------Reemplazando {simbolo} -----------------')
    for col in col_con_simbolo:
            data[col].loc[data[col]==simbolo] = np.nan
            print(f'reemplazado en {col}')
    if dev_listas:
        return col_con_simbolo, col_sin_simbolo

# Analisis univariado

# gracico variables continuas
def graficar_cont(data, lista_variables, distr='density',figura=(10,30), sep_plot=0.4): 
    '''
    Grafica variables continuas mostrando su media y mediana,
    con la curva de tendencia normal.
    '''
    fig = plt.figure(figsize=figura)  # tamaño de la figura
    fig.subplots_adjust(hspace=sep_plot)  # ajuste de las subplots

    for n, col in enumerate(lista_variables):
        plt.subplot(len(lista_variables), 1, n+1)
        sns.histplot(data[col], stat=distr, color='royalblue')
        if distr=='density':
            sns.kdeplot(data[col], color='tomato', lw=1)
        plt.axvline(data[col].mean(), color='green', label='media')
        plt.axvline(data[col].median(), color='black', label='mediana')
        plt.title(col)
        plt.xlabel("")
        plt.legend()
        plt.tight_layout()

# Analisis mixto (univ + multiv)

# Graficar outliers boxplot vs scaterplot
def box_scater(df, parametros, vec_obj, figura=(10,30), sep_plot=0.4):
    '''
    Grafica la variable y la variable vs vector objtivo en un 
    scaterplot y un boxplot
    [Params]
    [df]: [objeto pandas]: data frame
    [parametros]: [lista]: columnas sin el vector obj
    [vec_obj]: [str]: nombre del vector obj
    '''
    fig = plt.figure(figsize=figura)  # tamaño de la figura
    fig.subplots_adjust(hspace=sep_plot)  # ajuste de las subplots
    filas = len(parametros)
    j = 2
    n = 1
    for param in parametros:
        plt.subplot(filas, 2, n)
        sns.scatterplot(data=df, y=vec_obj, x=param)
        plt.subplot(filas, 2, j)
        sns.boxplot(data=df, x=param)
        j += 2
        n += 2

#contar nan
def contar_nan(data, lista_nulos):
    ''' 
    Ingresa una data y una lista de columnas
    para imprimir los % de nan por columnas, y el total porlineas       
    '''
    for col in lista_nulos:
        nulos = data[col].isnull().value_counts("%")
        try:
            nulos = nulos[True]*100
            print(f'{col}: {np.round(nulos,4)}%\n')
        except:
            print(f'{col}: sin nulos')
    tmp_drop = data.dropna().copy()
    porcion_nulos = (1-(tmp_drop.shape[0]/data.shape[0]))*100
    print(f'% de lineas con nan en la data {np.round(porcion_nulos,4)}%')


