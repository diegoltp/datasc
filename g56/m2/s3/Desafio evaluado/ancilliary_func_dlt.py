import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def valores_perdidos(dataframe, var:str, print_list:bool=False):
    '''
    df: Data Fame
    var: Columna a inspeccionar
    print List: True si es que quieres imprimir
    '''

    df = dataframe.copy()
    valores_faltantes = df[var].isna().sum()
    valores_totales = len(df[var])
    if print_list:
        print(f'''
{var}
------------------------------------------
{np.round(df[var], 4).to_list()}''')
    return valores_faltantes, valores_faltantes/valores_totales*100

def imprime_info_na(dataFrame, lista_columnas, print_list=False):
    for columna in lista_columnas:
        print(f"{columna}: {valores_perdidos(dataFrame, columna, print_list)}")

def graficar_1(sample_df:pd, full_df:pd, var:str, true_mean:bool, sample_mean:bool=False):
    plt.hist(sample_df[var], color='royalblue')
    plt.title(f'Histograma Muestra aleatoria columna: {var}')
    if sample_mean:
        plt.axvline(sample_df[var].mean(), color='tomato', lw=2, linestyle='--', alpha=0.75,
                    label='Muestra')
    if true_mean:
        plt.axvline(full_df[var].mean(), color='green', lw=2, linestyle='--', alpha=0.75,
                    label='Poblacion')
    plt.legend()

def grafico_puntos(dataFrame:pd, plot_var:str, plot_by:str, statistic:str='mean', global_stat:bool=False):
    '''
    dataFrame:pd Data Fame
    plot_var:str columna de la cual se obtiene la metrica
    plot_by:str Columna por la cual se agrupara el DF
    statistic:str='mean' [mean, median] valor estadistico a calcular
    global_stat:bool=False True= Graficar el statistic de la variable sin agrupar
    '''
    if statistic == 'mean':
        if global_stat:
            plt.axvline(dataFrame[plot_var].mean(), color='tomato', linestyle='--')
            
        df_agrupada = dataFrame.groupby(plot_by)[plot_var].mean()
        plt.plot(df_agrupada.values, df_agrupada.index, 'o', color='green')
    if statistic == 'median':
        if global_stat:
            plt.axvline(dataFrame[plot_var].mean(), color='tomato', linestyle='--')
        
        df_agrupada = dataFrame.groupby(plot_by)[plot_var].median()
        plt.plot(df_agrupada.values, df_agrupada.index, 'o', color='green')

