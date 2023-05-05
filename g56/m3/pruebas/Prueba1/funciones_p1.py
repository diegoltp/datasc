import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score


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

#entrenar CV
def df_palabras_frecuencia(cv_definido, df_palabras):
    '''  
    [resumen] : entrena el cv_definido con los datos df_palabras y genera df.
    [cv_definido] : CountVectorizer con sus parametros definidos
    [df_palabras] : df['contenido'] data de la columna que contiene las palabras
    [Returns] : dataframe con palabras y frecuencias.
    '''
    cv_fit = cv_definido.fit_transform(df_palabras)
    words = cv_definido.get_feature_names_out()
    word_frequency = cv_fit.toarray().sum(axis=0)
    words_freq_df= pd.DataFrame([list(words), list(word_frequency)]).T
    words_freq_df.columns = ['word', 'freq']
    return words_freq_df.sort_values(by='freq')

#Analisis de df extraida
def detalle_freq1(df_freq, columna='freq', muestra=15, minfreq=1):
    '''
    Imprime muestra de palabras con frecuencia 1 y su porcentaje
    [df_freq]: df con columnas llamadas columnas [word, freq]
    [columna]: columna con frecuencias
    [muestra]: tamaño muestra de palabras
    [return]: informacion
    '''
    valores_fq1 = df_freq.loc[df_freq[columna]<=minfreq].shape[0]
    porcent_fq1 = (valores_fq1/df_freq.shape[0])*100
    print(f'Contiene {valores_fq1} elementos con frecuencia igual o menor a {minfreq}: {porcent_fq1:.2f} %')
    print(df_freq.loc[df_freq[columna]<=minfreq].sample(muestra))

#Graficar por categoria y frecuencia de palabras
def word_count_by_clasif(cv, df, col_oracion, col_clasif, clasificacion, sort_n=100):
    tmp_vect = cv
    tmp_fit_transform = tmp_vect.fit_transform(df[df[col_clasif] == clasificacion][col_oracion])
    tmp_words = tmp_vect.get_feature_names_out()
    tmp_frequencies = tmp_fit_transform.toarray().sum(axis=0)
    tmp_df = pd.DataFrame([list(tmp_words), list(tmp_frequencies)]).T
    tmp_df.columns = ['words', 'freq']
    tmp_df = tmp_df.sort_values(by='freq', ascending=False).iloc[0:sort_n, :]
    plt.barh(tmp_df['words'], tmp_df['freq'])

#modelacion previa
def modelacion_inicial(modelo, X, y, guardar=False, entrenar=True):
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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=1991)
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


#Metricas
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

#pruebas
def prueba_tweets(tweet,cv_entrenado, pca_entrenado, modelo):
    '''
    Recibe un texto para clacificar positivo o negativo
    [tweet]: texto a analizar
    [cv_entrenado]: Count vectorizer u otro metodo de extraccionde palabras entrenado
    [pca_entrenado]: PCA para reducir dimension entrenado
    [modelo]: Modelo predictor
    '''
    tweet_vect = cv_entrenado.transform([tweet]).toarray()

    # Reducir la dimensionalidad de los vectores
    project_tw = pca_entrenado.transform(tweet_vect)
    tw_redu_c = pd.DataFrame(project_tw)

    # Predecir la polaridad de los tweets
    tweet_polarity = modelo.predict(tw_redu_c)
    print("Polaridad del tweet: ", ['Positivo' if tweet_polarity[0]==1 else 'Negativo'])

def prueba_tweets_nb(tweet,cv_entrenado, modelo):
    '''
    Recibe un texto para clacificar positivo o negativo
    [tweet]: texto a analizar
    [cv_entrenado]: Count vectorizer u otro metodo de extraccionde palabras entrenado
    [modelo]: Modelo predictor
    '''
    tweet_vect = cv_entrenado.transform([tweet]).toarray()

    # Predecir la polaridad de los tweets
    tweet_polarity = modelo.predict(tweet_vect)
    print("Polaridad del tweet: ", ['Positivo' if tweet_polarity[0]==1 else 'Negativo'])