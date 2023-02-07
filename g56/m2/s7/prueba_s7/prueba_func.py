#ignorar alertas de deprecacion
import warnings
warnings.filterwarnings("ignore")
#manejo de base de datos y funciones estadisticas
import pandas as pd
import numpy as np
#Generar graficas y estilos de graficos.
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

#Manejo y visualizacion de datos perdidos
import missingno as msngo
#imputar datos para los valores perdidos
from sklearn.impute import SimpleImputer

#Generar modelos
from sklearn import linear_model
import statsmodels.formula.api as smf
#Generar y entrenar modelos de clasificacion, regresion logistica
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split #dividir matriz de test-train
from sklearn.preprocessing import StandardScaler #entrnar modelo

# Metricas
from sklearn.metrics import classification_report, roc_curve
from sklearn.metrics import roc_auc_score
import factor_analyzer as fact #prueba de esfericidad y KMO
from sklearn.metrics import mean_squared_error, r2_score # Metricas de regresion
from sklearn.model_selection import cross_val_score #indicadores comparacion

# Funciones Clasificacion
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

# gracico variables continuas
def graficar_cont(data, lista_variables, distr='density'): 
    '''
    Grafica variables continuas mostrando su media y mediana,
    con la curva de tendencia normal.
    '''
    for n, col in enumerate(lista_variables):
        plt.figure(figsize=(7,10))
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
#imputador
def entrenar_imputador(data:pd, strategy:str,dev_matriz=False, missing_val=np.nan, tamaño_test=0.33, random=1991):
    ''' 
    Input:
    data:[pd.Series]: Base de datos o vector
    strategy:[str]: Estrategias permitidas por SimpleImputer de Sklearn
    missing_val=np.nan [opc]
    dev_matriz=False [opc]
    tamaño_test=0.33 [opc]
    random=1991 [opc]
    Return:
    imp: Modelo entrenado a partir de sub matriz para reemplazar missing_val
    x_train: Sub matriz de entrenamiento
    x_test: Sub matriz de prueba
    df_clean: Base de datos sin valores perdidos.
    '''
    x_train, x_test = train_test_split(data, test_size=tamaño_test, random_state=random)
    imp = SimpleImputer(missing_values=missing_val, strategy=strategy)
    imp.fit_transform(x_train)
    df_tmp = data.copy()
    df_clean = pd.DataFrame(imp.transform(df_tmp), columns=data.columns)
    if dev_matriz:
        return imp, x_train, x_test, df_clean
    else:
        return imp, df_clean

# concatena elementos de una lista con un +
def gen_regresores(data_or_list, y):
    '''    
    No utilizar si no es una DF o Lista!
    Devuelve una cadena STR con los regresores concatenados por un +
    data_or_list[Pd.Series] or [list]: Origen de datos.
    y[str]: columna vector objetivo.
    '''
    try:
        tmp=list(data_or_list.columns.values)
    except:
        tmp=data_or_list.copy()
    [tmp.remove(y) if y in tmp else tmp]
    return '+'.join(tmp)

# Remueve variables de una lista en base a la confianza P-value
def remover_variables(columnas, modelo_log, confianza:float=0.05, test='P>|z|'):
    '''  
    Remueve variables de una lista en base a la confianza P-value
    lista[list]: lista de todas las variables
    modelo_log[statsmodels.discrete.discrete_model.BinaryResultsWrapper]
    confianza[float]: Nivel de la prueba de confianza
    Return:
    Entrega lista depurada de variables 
    e imprime un check_in del subconjunto vs la lista madre.
    '''
    #genera lista con variables a remover segun p_value
    m1_no_sign = modelo_log.summary2().tables[1][test]
    var_to_remove = list(m1_no_sign[m1_no_sign > confianza].index)
    #genera lista con variables no significativas removidas
    tmp_column = columnas.copy()
    for col in var_to_remove:
        tmp_column.remove(col)
    for i in columnas:
        x = [True  if i in tmp_column else False]
        print(f'{i}: {x}')
    return tmp_column

#entrega indicadores especificos de comparacion del modelo
def validar_modelos(modelo):   
    ''' 
    Entrega indicadores especificos de comparacion del modelo
    modelo: modelo de regresion
    ''' 
    tmp_index = list(modelo.params.index)
    fit = pd.DataFrame({'Statistics': modelo.summary2().tables[0][2][0:],
    'Value': modelo.summary2().tables[0][3][0:]})
    print(f'''
parametros: {tmp_index}
{fit}
-------------------------------''')

# funcion inversa logg_odds
def inverse_logit(x):
    return 1 / (1+np.exp(-x))

#Pasa log-odds en probabilidad dado un modelo
def calcular_prob(modelo, primeros_x_eval:int=5):
    '''
    Pasa log-odds en probabilidad dado un modelo
    modelo[statsmodels.discrete.discrete_model.BinaryResultsWrapper]
    primeros_x_eval[int]: [opc=5]: Los 'x' primeros 
    '''
    primeros_x_eval = primeros_x_eval+1
    #lista de los mejores p values
    p_value_ascending = modelo.summary2().tables[1]['P>|z|'].sort_values(ascending=True)
    mejores_x = list(p_value_ascending[:primeros_x_eval].index)
    odd_interc = 0
    for parametro in mejores_x:
        if parametro == 'Intercept':
            odd_interc = modelo.params[parametro]
            prob_interc = inverse_logit(odd_interc)*100
            print(f'''La probabilidad de ganar mas de 50K usd al año,
    sin tener variables es de {prob_interc:,.5f}%
    ''')
        else:
            prob_y_best = inverse_logit(modelo.params[parametro]+odd_interc)*100
            print(f'''La probabilidad de ganar mas de 50K usd al año,
        dado {parametro} es de {prob_y_best:,.5f}%
        ''')

#Crear matrices y entrena modelo
def train_modelo_ml(data, vector_x, column_y, size=0.33, state=1991):
    '''
    Crea las matrices X_train, X_test, y_train, y_test
    luego entrena el modelo con x_test
    data[DataFrame], vector_x[list], column_y[list]
    '''
    df_x = data.loc[:,vector_x].copy()
    df_y = data.loc[:,[column_y]].copy()
    X_train, X_test, y_train, y_test = train_test_split(df_x,df_y,test_size=size,random_state=state)
    
    X_train_std = StandardScaler().fit_transform(X_train)
    X_test_std = StandardScaler().fit_transform(X_test)
    mod_entrenado = LogisticRegression().fit(X_train_std, y_train)

    yhat = mod_entrenado.predict(X_test_std)
    yhat_pr = mod_entrenado.predict_proba(X_test_std)
    return mod_entrenado, y_test, yhat, yhat_pr

# Imprime tablas con indicadores
def indicadores_ml(y_test, y_hat, yhat_pr):
    '''      
    Imprime tablas y graficos con indicadores.
    '''
    print(classification_report(y_test, y_hat))
    false_positive, true_positive, threshold = roc_curve(y_test, yhat_pr[:, 1])
    plt.title('Curva ROC')
    plt.plot(false_positive, true_positive, lw=1)
    plt.plot([0, 1], ls="--", lw=1)
    plt.plot([0, 0], [1, 0] , c='limegreen', lw=3), plt.plot([1, 1] ,c='limegreen', lw=3)
    plt.ylabel('Verdaderos Positivos')
    plt.xlabel('Falsos Positivos')
    print(f'Area bajo la curva: {roc_auc_score(y_test, yhat_pr[:, 1])}')

# desafio 2 regresion

def prueba_kmo(data, criterio=0.7): 
    '''
    Ingresa vectores a evaluar con un criterio determinado
    imprime si la variable pasa la prueba o no.
    '''
    lista_kmo = fact.calculate_kmo(data)
    for n, i in enumerate(lista_kmo[0]):
        if i <= criterio:
            print(f'{data.columns[n]} : {np.round(i,3)}=> no pasa')
        else:
            print(f'{data.columns[n]}: {np.round(i,3)} => Pasa')
    print(f'Modelo: {np.round(lista_kmo[1],3)}')

#Crear matrices y entrena modelo
def train_modelo_linear(data, vector_x, column_y, size=0.33, state=1991, intercepto=True):
    '''
    Crea las matrices X_train, X_test, y_train, y_test
    luego entrena el modelo con x_test
    data[DataFrame], vector_x[list], column_y[list]
    '''
    df_x = data.loc[:,vector_x].copy()
    df_y = data.loc[:,[column_y]].copy()
    X_train, X_test, y_train, y_test = train_test_split(df_x,df_y,test_size=size,random_state=state)
    
    modelo = linear_model.LinearRegression(fit_intercept=intercepto)
    modelo.fit(X_train, y_train)
    yhat = modelo.predict(X_test)

    return modelo, y_test, yhat

#obtiene metricas lineales
def metricas_ml_linear(y_test, y_hat):
    '''
    obtiene metricas para modelo de regresion lineal
    '''
    m1_mse = mean_squared_error(y_test, y_hat).round(1)
    m1_r2 = r2_score(y_test, y_hat).round(2)
    print(f'Mean Squared Error:  {m1_mse}')
    print(f'R-cuadrado:  {m1_r2}\n')
#Metricas cruzadas
def graficar_indicadores(eval_metrics, df_mod, list_mod, lista_id, vector_y):
    '''
    aplica funcion cross_val_score dado los modelos de analisis
    (diseñado para solo 3 modelos)
    eval_metrics:[list]:Metricas a evaluar, validas en 3.3. Metrics and scoring
    df_mod:[DataFrame]:Base de datos del modelo
    list_mod:[list[list][str]]:Lista contenedora de lista con columnas del modelo
    lista_id:[list]:lista con nombre para cada modelo
    vector_y:[str]: vector objetivo
    '''
    plt.subplots(1, len(eval_metrics))
    plt.xticks(rotation=70)
    for n, i in enumerate(eval_metrics):
        tmp_1 = cross_val_score(linear_model.LinearRegression(), df_mod.loc[:,list_mod[0]],
                        df_mod.loc[:,vector_y], cv = 10, scoring = i)
        tmp_2 = cross_val_score(linear_model.LinearRegression(), df_mod.loc[:,list_mod[1]],
                            df_mod.loc[:,vector_y], cv=10, scoring=i)
        tmp_3 = cross_val_score(linear_model.LinearRegression(), df_mod.loc[:,list_mod[2]], 
                            df_mod.loc[:,vector_y], cv=10, scoring=i)
        tmp = pd.DataFrame({lista_id[0]: tmp_1,
        lista_id[1]: tmp_2,
        lista_id[2]: tmp_3}).unstack().reset_index()
        tmp.rename(columns={'level_0':'order',
        'level_1': 'num',
        '0': 'score'}, inplace=True)
        plt.subplot(1, 3, n+1)
        sns.boxplot(tmp.iloc[:,0],
        tmp.iloc[:, 2])
        sns.despine()
        plt.xticks(rotation=45, ha='right')
        plt.xlabel(' ')
        plt.ylabel(' ')
        plt.title(i.capitalize())
        plt.tight_layout()