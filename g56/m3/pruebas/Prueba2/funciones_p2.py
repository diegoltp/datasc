import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

#Dividir matriz de datos
from sklearn.model_selection import train_test_split 

#imputar datos para los valores perdidos
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score,classification_report, roc_curve, auc, f1_score, precision_score, recall_score


#estudiar perdidos
def estudio_nulos(data, simbolo):
    ''' 
    [resumen]: Imprime cantidad de perdidos en cada columna y devuelve listas,
               todo en base al simbolo proporcionado
    [data]: DataFrame
    [simbolo]: Caracter, string, valor a buscar como nulo o perdido
    [return]: lista_sincaract, lista_concaract
    '''
    lista_sinvacios = []
    lista_convacios = []
    for i in data.columns:
        try:
            print(f'{i}: {data[i].value_counts()[simbolo]}')
            lista_convacios.append(i)
        except:
            lista_sinvacios.append(i)
    return lista_sinvacios, lista_convacios

#conteo de np.nan
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

#imputar datos perdidos
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
    
#info columnas proactiva 
def separar_columnas(data, min_filas=2,max_col=5):
    '''  
    [Resumen]:  Separ columnas por tipo, object o int/float
                Imprime largos y nro de columnas propuestas para graficar
    [data]:     dataFrame.
    [max_col]: maximo numero de columnas en grafico
    [return]
    [lista_objects]: lista columnas object.
    [lista_numeros]: lista columnas numeros.

    '''
    #Crear list
    lista_objects, lista_numeros, otro = [] , [] , []

    for index, row in data.items():
        if row.dtype == object:
            lista_objects.append(index)
        elif row.dtype == 'float64' or row.dtype =='int64':
            lista_numeros.append(index)
        else:
            otro.append(index)
    print(f'Columnas en Obj: {len(lista_objects)}, en numero: {len(lista_numeros)}, otro: {len(otro)}')
    #grillas obj
    filas = min_filas
    m_col = max_col
    columnas = len(lista_objects)/filas
    print('\nGrillas posibles obj:')
    while m_col >=1 and columnas>=1:
        print(f'Filas = {filas}, Columnas = {np.ceil(columnas)}')
        filas += 1
        columnas = len(lista_objects)/filas
        m_col -= 1
    
    #grillas nro
    filas = min_filas
    m_col = max_col
    columnas = len(lista_numeros)/filas
    print('\nGrillas posibles numericas:')   
    while m_col >=1 and columnas>=1:
        print(f'Filas = {filas}, Columnas = {np.ceil(columnas)}')
        filas += 1
        columnas = len(lista_numeros)/filas
        m_col -= 1
    return lista_objects, lista_numeros

#Graficar atributos
def graficar_cont(data, lista_variables, distr='freq',figura=(10,30), sep_plot=0.4, cols=1): 
    '''
    Grafica variables continuas mostrando su media y mediana,
    con la curva de tendencia normal.
    '''
    filas = int(np.ceil(len(lista_variables) / cols))
    fig = plt.figure(figsize=figura)  # tamaño de la figura
    fig.subplots_adjust(hspace=sep_plot)  # ajuste de las subplots

    for n, col in enumerate(lista_variables):
        plt.subplot(filas, cols, n+1)
        sns.histplot(data[col], stat=distr, color='royalblue')
        if distr=='density':
            sns.kdeplot(data[col], color='tomato', lw=1)
        plt.axvline(data[col].mean(), color='green', label='media')
        plt.axvline(data[col].median(), color='black', label='mediana')
        plt.title(col)
        plt.xlabel("")
        #plt.legend()
        plt.tight_layout()
    plt.legend()

#p1   
#grafico vec obj
def graficar_porcentajes_cat(vector_obj):
    '''
    [resumen] Grafica % de las categorias dentro del vector_obj
    [vector_obj] <- vector o columna del dataframe a graficar
    [return] grafico de barras horizontal
    '''
    values = [round(val*100, 2) for val in vector_obj.value_counts('%').values]
    value_labels = [str(val) + '%' for val in values]
    fig, ax = plt.subplots()
    vector_obj.value_counts('%').plot(kind='barh', ax=ax)
    for i, bar in enumerate(ax.patches):
        ax.annotate(value_labels[i], (bar.get_width(), bar.get_y() + bar.get_height() / 2))

def pipe_df_test(df):
    ''' funcion especifica para matriz test entregada'''
    #crear VO
    df['violmade'] = df.filter(regex='^pf_').apply(lambda row: row.str.contains('Y').any(), axis=1).astype(str)

    # Recodificaciones p1
    df['offverb'] = np.where(df['offverb'] == ' ', 'N', df['offverb'])
    df['offshld'] = np.where(df['offshld'] == ' ', 'N', df['offshld'])
    df['officrid'] = np.where(df['officrid'] == ' ', 'N', df['officrid'])
    df['trhsloc'] = np.where(df['trhsloc'] == ' ', 'OTRO', df['trhsloc'])

    # Recodificaciones p2
    df['time_bin'] = np.where((df['timestop'] > 1175), 'pick', 'valley')
    df['age_bin'] = np.where((df['age'] >=19) & (df['age'] <= 34), 'Y', 'N')
    df['weight_bin'] = np.where((df['weight'] >=150) & (df['weight'] <= 180), 'Y', 'N')
    df['ht_feet_bin'] = np.where((df['ht_feet'] == 5), 'Y', 'N')
    df['perobs_bin'] = np.where((df['perobs'] <= 3), 'Y', 'N')
    df['perstop_bin'] = np.where((df['perstop'] <= 3), 'Y', 'N')

    #categorias
    #Diccionario recod gla
    crimen_recod = {' ':'NA',
                '1050.7J':'1050',
                'CPW':'CPW',
                'CPCS':'CPCS',
                'GLA':'OTRO',
                'CRIM TRES':'CRIM TRES',
                'CRIM TRES/UPM':'CRIM TRES',
                'CPM':'CPM',
                '221.10':'221',
                'ROBBERY':'ROBBERY',
                'ROW':'ROW',
                'ASSAULT':'ASSAULT',
                '511.1A':'511',
                'CPCS,CPM5':'CPM',
                'DISCON':'OGA',
                'PL165.15 (3)':'165',
                '155.25':'155',
                '265.02':'265',
                '145.60':'145',
                '160.05':'160',
                'UNK':'OTRO',
                '511':'511',
                'RESIST/DISCON':'DISCON',
                'CRIMINAL TRESPASS':'CRIM TRES',
                '165.15(3)':'165',
                'P.L. 240.20':'240',
                'UNAUTHORIZED':'CRIM TRES',
                'CPW 4':'CPW',
                'CPM 5':'CPM',
                'CPW 2':'CPW',
                'GRAND LARC':'GRAND LARCENY',
                'P.L. 140.15':'140',
                'CT/CPM':'CPM',
                'BURGLARY':'BURGLARY',
                '265':'265',
                'ATT BURGLARY':'BURGLARY',
                'CPCS 7TH':'CPCS',
                'PL 265.03 CPW':'CPW',
                'CRIMINAL MISCHIEF':'CRIMINAL MISCHIEF',
                'CSM':'OTRO',
                'TRESPASS':'CRIM TRES',
                'PL 155.25':'155',
                'FORGED INSTRUMENT':'UNLIC',
                '140.15':'140',
                '10-125 2B':'10-125',
                'FRAUD ACCOSTING, GRANDLARCENY':'GRAND LARCENY',
                'TOS':'OTRO',
                'PL165.4':'165',
                '265.01':'265',
                '221.01':'221',
                '140.10':'140',
                'PL 120.00':'120',
                '221-10':'221',
                '170.25 / 140.35':'140',
                '165.15 3':'165',
                '160.10':'160',
                '220.16':'220',
                '155.25 145.00':'155',
                'CRIM TRESPASS':'CRIM TRES',
                'PROSTITUTION':'PROSTITUTION',
                '130.52':'130',
                'PL  130.52':'130',
                'CPCS7':'CPCS',
                '221.0':'221',
                'CRI TRES':'CRIM TRES',
                'RETURN ON WARRANT':'WARRANT',
                '165 15 (3)':'165',
                'UNLIC GENERAL VENDOR':'UNLIC',
                'AGG. PANHANDLING':'OTRO',
                'PL 24.20':'OTRO',
                'CRIM COUNTERFIET':'OTRO',
                'GRAND LARCENY AUTO':'GRAND LARCENY',
                'CPCS 3 CRIM TRESPASS':'CRIM TRES',
                'ASSAULT 3':'ASSAULT',
                'OPEN CONTAINER':'CRIM TRES',
                'CPSP / GRAFITTI':'CPSP',
                'CRIM TRESS':'CRIM TRES',
                'PL':'OTRO',
                '120.20':'120',
                '140.10/ROW':'ROW',
                'GRAND LARCENY':'GRAND LARCENY',
                'AC 153.09':'OTRO',
                '120.25':'120',
                'OGA':'OGA',
                '220.06':'220',
                '245.00':'OTRO',
                '140.10 P.L.':'140',
                'UNLIC VENDOR':'OTRO',
                '215.40':'OTRO',
                'MAKING GRAFFITI':'OTRO',
                'ASSLT':'ASSAULT',
                'ROBBERY 2':'ROBBERY',
                'PETIT LARCENYE':'PETIT LARCENY',
                'PL 120.00(1)':'120',
                'OGA DISCON':'OGA',
                'ROB 2':'ROBBERY',
                'UNKOWN':'OTRO',
                '140.10 PL':'140',
                'CRIMINAL TRESSPASS':'CRIM TRES',
                '165.15':'165',
                'PETIT LARCENY':'PETIT LARCENY',
                'PL155.25':'155',
                'THEFT OF SERVICE':'OTRO',
                'ASSAULT  3':'ASSAULT',
                '10-133B,  205.30':'OTRO',
                'CPCS 7':'CPCS',
                '221.40':'221',
                'CPSP':'CPSP',
                '16571':'165',
                'CPM3':'CPM',
                '145.05':'145',
                'CPFI':'OTRO',
                'AGG. LIC.':'OTRO',
                '165.10':'165',
                '145.60 02':'145',
                'CRIMINAL POSSESSION OF WEAPON':'OTRO',
                'DICSON':'OGA',
                'RECKLESS ENDANGERMENT':'OTRO',
                "OBSTRUCT GOV'T ADMINISTRATION":'OTRO',
                '1050.9D':'1050',
                '170.25':'170',
                '220.16PL':'220',
                'PL 145.05 (2)':'145',
                'CSCS':'OTRO',
                'PL 221.10 PL 240.35 (2) PL 205':'221',
                'ASSAULT/CPW':'CPW',
                'CRIM MISC':'OTRO',
                'CRIM CONTEMPT':'OTRO',
                'XXX':'OTRO',
                'CPW 4DEGREE':'CPW',
                'CRIM. TRESS.':'CRIM TRES',
                'PL 165.15':'165',
                '170.15':'170',
                '221.15':'221',
                'UGV':'OTRO',
                'BURG':'BURGLARY',
                '265.01 CPW':'CPW',
                '1050.7(J)':'1050',
                '1192-1':'OTRO',
                '155.30 (1)':'155',
                '220.03':'220',
                '10-125':'10-125',
                '160.10 (01)':'160',
                'SEX ABUSE':'SEX ABUSE',
                '221.40 / 221.05':'221',
                'CRIMINAL  TRESSPASS':'CRIM TRES',
                'ASS':'ASSAULT',
                'CRIMINAL TAMPERING':'OTRO',
                'CRIM TRES & CPCS 7':'CRIM TRES',
                'PL 265.02':'265',
                'CRIM IMPER':'OTRO',
                'ASSAULT 2':'ASSAULT',
                'FALSE PERS/WARRANT':'WARRANT',
                'CPM/CRIM TRES':'CPM',
                'CPCS/TAMP W/ EVIDENCE':'CPCS',
                '10-118 B':'OTRO',
                'CPCS 3':'CPCS',
                '240.10':'240',
                '221.05/ROW':'ROW',
                'CPW 265.01':'CPW',
                'CT':'CRIM TRES',
                '20-465 (B) / WARRANT':'WARRANT',
                '190.25':'OTRO',
                'ASSAULT ON PO':'ASSAULT'}
    offen_recod = {' ':'NA',
              'UNREASONABLE NOISE':'UNREASONABLE NOISE',
              'DISORDERLY CONDUCT':'DISORDERLY CONDUCT',
              '240.20 (5)':'240',

              '1110A VTZ':'OTRO',
              '65 C1':'OTRO',
              '10-125 (2)B':'10-125',
              'OPERATING BIKE ON SIDEWALK':'DRIVING BAD',

              'DIS CON':'DISCON',
              '37512AB':'OTRO',
              'TRESPASS':'TRESPAS',
              '10-125':'10-125',
              '19-176B':'19-176',
              '240.35':'240',

              'OPEN CONTAINER':'OPEN ALCOHOL',
              '10-125 2B':'10-125',
              '240.20':'240',
              'NO PLATE':'DRIVING BAD',

              'OPEN CONATINER':'OPEN ALCOHOL',
              'VTL1212':'OTRO',
              '10-125(2)':'10-125',
              '19.176 (B)':'OTRO',

              '10-125(2B)':'10-125',
              'DISCON':'DISCON',
              'DISOBEYING PARK RULES':'DRIVING BAD',
              'UPM':'OTRO',
              '375-':'OTRO',

              '140-05':'140',
              '1-03C2':'PRR1-03',
              '24-163':'OTRO',
              '19-176 C':'19-176',
              '509.1':'OTRO',
              '16-118.6':'OTRO',

              'ALCOHOL':'OPEN ALCOHOL',
              'OPEN CONT':'OPEN ALCOHOL',
              '161.04':'OTRO',
              'DIS-CON':'DISCON',
              'UNLIC OP':'OTRO',

              'UNDER 21 POSSESS ALCOHOL':'OPEN ALCOHOL',
              '140.05':'140',
              'UNREASONALBE NOISE':'UNREASONABLE NOISE',

              '10-1251 2B':'10-125',
              '1229 C 3 A':'OTRO',
              '140.50':'140',
              'IMPROPER PLATE':'DRIVING BAD',

              'HC 153.09':'OTRO',
              'TRESPASSING':'TRESPAS',
              '221.05':'221.05',
              '12259C2A VTL':'OTRO',

              '10-125 (2B)':'10-125',
              '1-03 CD2':'PRR1-03',
              '240.20 (7)':'240',
              '240.20.5':'240',
              '103-2':'OTRO',

              '153-09':'OTRO',
              '10-134(1) BOXCUTTER':'ARMA BLANCA',
              'PARK AFTER DUSK':'DRIVING BAD',
              '240.20 7':'240',

              '19-176':'19-176',
              '1050.9D':'OTRO',
              'URINE IN PUBLIC':'URINATING IN PUBLIC',
              '240.20 1PL':'240',
              'AC 24-218':'OTRO',

              '10-133':'OTRO',
              'LITTERING':'URINATING IN PUBLIC',
              '1110A VTL':'OTRO',
              'SUSPENDED REG':'OTRO',
              '10125(2)(B)':'OTRO',

              'PL 240.20':'240',
              '10-125 2(B) AC':'10-125',
              'VTL':'OTRO',
              '161-':'OTRO',
              '240-20':'240',

              'TINTED GLASS':'DRIVING BAD',
              '509 1':'OTRO',
              '193176.26':'OTRO',
              '1-03 C(2)':'PRR1-03',
              'POSS KNIFE':'ARMA BLANCA',

              '10-137':'OTRO',
              '10-25-2-B':'OTRO',
              'URINATING IN PUBLIC':'URINATING IN PUBLIC',
              'OUTSTRETCHED':'OTRO',

              'BOXCUTTER IN PUBLIC':'ARMA BLANCA',
              'MACE':'OTRO',
              'OPEN CONT ALCOHOL':'OPEN ALCOHOL',
              '10.125.2 (B)':'OTRO',

              '240.20 SUB 5':'240',
              '101252B':'OTRO',
              '19-176 (B)':'19-176',
              'RUNNING RED LIGHT':'DRIVING BAD',

              'TRESSPASS':'TRESPAS',
              '1310-PHL':'OTRO',
              'ILLEGAL WINDOW TINT':'DRIVING BAD',
              'DIS. CON':'DISCON',
              'BOS':'OTRO',

              'THEFT OF SERVICE':'THEFT OF SERVICE',
              '1-03':'PRR1-03',
              'DIS COM':'DISCON',
              '10-118 SUB B':'OTRO',
              '1042510':'OTRO',
              'DISCON- 240.20 (5)':'DISCON',
              'UNLICENSED DRIVER':'DRIVING BAD',
              'BIKE ON SIDEWALK':'DRIVING BAD',

              'KNIFE IN PUBLIC VIEW':'ARMA BLANCA',
              '161.05':'OTRO',
              '1010 VTL':'OTRO',
              'PL 240.20 (5)':'240',

              'VTL11104':'OTRO',
              '1212 VTL':'OTRO',
              'RUN STOP SIGN':'DRIVING BAD',
              'UNKNOWN':'DISCON',
              '1-63 C2':'OTRO',

              'CPW':'CPW',
              '240.20 (3)':'240',
              'AC 19476 (C)':'OTRO',
              '153.09':'OTRO',
              'RECKLESS DRIVING':'DRIVING BAD',

              'DIS CON.':'DISCON',
              'DISCON 240.20':'DISCON',
              'PUBLIC URINATION':'URINATING IN PUBLIC',
              'PRR 1-03':'PRR1-03',

              'PRR 1-03 C2':'PRR1-03',
              '24-227':'OTRO',
              '1-03 C2':'PRR1-03',
              '240.20(1)':'240',
              'CPM':'CPM',
              '181.03':'OTRO',

              '19-176 (C) AC':'19-176',
              'DRIVING ON CELL PHONE':'DRIVING BAD',
              '16-118(1) AC':'OTRO',
              '24-218':'OTRO',

              '240.20 (50':'240',
              'DISCON 240.201':'240',
              'CELL PHONE':'DRIVING BAD',

              'KNIFE IN PUBLIC VIEW (DISCON)':'ARMA BLANCA',
              'OPER BIKE SIDEWALK':'DRIVING BAD',
              'STOP SIGN':'DRIVING BAD',

              'AC10-120':'OTRO',
              'DISCON 240.20-5':'240',
              '1225C2A':'OTRO',
              '125-2B':'OTRO',
              'NO INSURANCE':'DRIVING BAD',

              'FAILURE TO OBEY RULE':'OTRO',
              'A.C. 10-125 2(B)':'10-125',
              'AC 16-122(C)':'OTRO',

              '1050.7J':'OTRO',
              '319.1':'OTRO',
              'PL 140.05':'140',
              'TINTS':'DRIVING BAD',
              '10125-2B':'OTRO',

              'PARK AFTER DARK':'DRIVING BAD',
              'NO ID':'NO ID',
              'PRR 103A2':'OTRO',
              '153.09 HC':'OTRO',
              '319-1':'OTRO',

              '240.20 ( 1 )':'240',
              '19176B':'OTRO',
              '19-506':'OTRO',
              'VTL 1125 A':'OTRO',
              '240.20 6':'240',

              'BICYCLE ON SIDEWALK':'DRIVING BAD',
              'LOITERING/GAMBLING':'OTRO',

              'ILLEGAL POSTING SIGNS':'OTRO',
              'VTL 319-1':'OTRO',
              'OPEN CONTAINER OF ALCOHOL':'OPEN ALCOHOL',

              'RIDING BIKE ON SIDEWALK':'DRIVING BAD',
              '1050.9(D)':'OTRO',
              'TINT':'DRIVING BAD',
              'AC 10-133':'OTRO',
              'UNK':'DISCON',

              '103-C2':'OTRO',
              '240.26 SUB 6':'240',
              'UTL 1172':'OTRO',
              'UNLEASHED DOG':'OTRO',

              '16-118 SUB 6':'OTRO',
              'PL 240.20(2)':'240',
              'FAIL TO AFFIX LIC PLATE':'DRIVING BAD',

              '19-121':'OTRO',
              '19-176 B':'19-176',
              '240.20 PL':'240',
              'PRR 1-04':'OTRO',

              'DIS CON - FIGHTING':'DISCON',
              '10-118 B':'OTRO',
              '153.04HC':'OTRO',
              'FARE EVASION':'DRIVING BAD',

              'LOUD NOISE':'UNREASONABLE NOISE',
              '10-125 2AA/C':'10-125',
              'P.L. 240.20    9010':'240',
              'VTL 809.01':'OTRO',

              'UNSAFERIDING':'DRIVING BAD',
              '19-1256 AC':'OTRO',
              '240-20(21)':'240'}
    
    df['arstoffn'] = df['arstoffn'].replace(crimen_recod)
    df['sumoffen'] = df['sumoffen'].replace(offen_recod)

    return df

def df1_vs_df2(df1, df2):
    ''' compara columnas de dos df
    devuelve lista con fiderencias df1 > df2
    '''
    lista = df1.columns.to_list()
    for i in df2.columns.to_list():
        if i in lista:
            lista.remove(i)
    return lista

def plot_classification_report(y_true, y_hat):
    """
    plot_classification_report: Genera una visualización de los puntajes reportados con la función `sklearn.metrics.classification_report`.

    Parámetros de ingreso:
        - y_true: Un vector objetivo de validación.
        - y_hat: Un vector objetivo estimado en función a la matriz de atributos de validación y un modelo entrenado.

    Retorno:
        - Un gráfico generado con matplotlib.pyplot

    """
    # process string and store in a list
    f1_score_value_0 = f1_score(y_true=y_true, y_pred=y_hat, pos_label=0)
    precision_score_value_0 = precision_score(y_true=y_true, y_pred=y_hat, pos_label=0)
    recall_score_value_0 = recall_score(y_true=y_true, y_pred=y_hat, pos_label=0)

    f1_score_value_1 = f1_score(y_true=y_true, y_pred=y_hat, pos_label=1)
    precision_score_value_1 = precision_score(y_true=y_true, y_pred=y_hat, pos_label=1)
    recall_score_value_1 = recall_score(y_true=y_true, y_pred=y_hat, pos_label=1)

    f1_score_value_avg = np.mean([f1_score_value_0, f1_score_value_1])
    precision_score_value_avg = np.mean([precision_score_value_0, precision_score_value_1])
    recall_score_value_avg = np.mean([recall_score_value_0, recall_score_value_1])


    colors = ['dodgerblue', 'tomato', 'purple', 'orange']

    plt.yticks([1.0, 2.0, 3.0], ['Precision', 'Recall', 'f1'])
    plt.xlim(0, 1)
    
    plt.plot(precision_score_value_0, [1], marker='x', color=colors[0])
    plt.plot(recall_score_value_0, [2], marker='x',color=colors[0], label=f'Class: {0}')
    plt.plot(f1_score_value_0, [3], marker='x', color=colors[0])

    
    plt.plot(precision_score_value_1, [1], marker='x', color=colors[1])
    plt.plot(recall_score_value_1, [2], marker='x',color=colors[1], label=f'Class: {1}')
    plt.plot(f1_score_value_1, [3], marker='x', color=colors[1])

    
    plt.plot(precision_score_value_avg, [1], marker='o', color='forestgreen')
    plt.plot(recall_score_value_avg, [2], marker='o', color='forestgreen', label='Avg')
    plt.plot(f1_score_value_avg, [3], marker='o', color='forestgreen')


def modelacion_inicial(modelo, X_train,X_test, y_train,y_test, guardar=False, entrenar=True):
    '''
    [resumen]: Separa matrices, entrena modelo clasificacion, imprime metricas,
    guarda modelo y metricas si guardar = True
    [modelo]: cualquier modelo sklearn de clasificacion, si entrenar = False ingresar best_params
    desde una busqueda de grilla
    [X]: Matriz atributos
    [y]: Vector objetivo
    [save_test]:[bool]:default=False, True= Guarda reportes
    [entrenar]:[bool] :Default = True, Flase=Salta el entrenamiento para cuando
    se hace una busqueda de grilla
    '''

    if entrenar == True:
        modelo.fit(X_train, y_train)
    reporte_train = classification_report(y_train,  modelo.predict(X_train))
    reporte_test = classification_report(y_test, modelo.predict(X_test))
    print(f'''Metricas en entrenamiento
    {reporte_train}
Metricas en Testeo
    {reporte_test}
    ''')
    if guardar == True:
        return reporte_train, reporte_test

def graficar_importancia(modelo, lista_col, nro_a_imprimir=10): 
    importancia = modelo.feature_importances_
    indices = np.argsort(importancia)[::-1]
    indices_10 = indices[0:nro_a_imprimir]
    names = [lista_col[i] for i in indices_10]
    plt.title("Feature importance")
    plt.barh(range(len(names)), importancia[indices_10])
    plt.yticks(range(len(names)), names, rotation=0)

    return names