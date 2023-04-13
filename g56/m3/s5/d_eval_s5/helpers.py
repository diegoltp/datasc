#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, roc_curve, auc, f1_score, precision_score, recall_score

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


def grid_plot_batch(df, cols, plot_type):

    """
    grid_plot_batch: Genera una grilla matplotlib para cada conjunto de variables.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame
        - cols: cantidad de columnas en la grilla.
        - plot_type: tipo de gráfico a generar. Puede ser una instrucción genérica de matplotlib o seaborn.

    Retorno:
        - Una grilla generada con plt.subplots y las instrucciones dentro de cada celda.

    """
    # calcular un aproximado a la cantidad de filas
    rows = int(np.ceil(df.shape[1] / cols))
    # para cada columna
    
    for index, (colname, serie) in enumerate(df.iteritems()):
        plt.subplot(rows, cols, index + 1)
        plot_type(x=serie)
        plt.tight_layout()

def identify_high_correlations(df, threshold=.7):
    """
    identify_high_correlations: Genera un reporte sobre las correlaciones existentes entre variables, condicional a un nivel arbitrario.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame, por lo general es la base de datos a trabajar.
        - threshold: Nivel de correlaciones a considerar como altas. Por defecto es .7.

    Retorno:
        - Un pd.DataFrame con los nombres de las variables y sus correlaciones
    """

    # extraemos la matriz de correlación con una máscara booleana
    tmp = df.corr().mask(abs(df.corr()) < threshold, df)
    # convertimos a long format
    tmp = pd.melt(tmp)
    # agregamos una columna extra que nos facilitará los cruces entre variables
    tmp['var2'] = list(df.columns) * len(df.columns)
    # reordenamos
    tmp = tmp[['variable', 'var2', 'value']].dropna()
    # eliminamos valores duplicados
    tmp = tmp[tmp['value'].duplicated()]
    # eliminamos variables con valores de 1 
    return tmp[tmp['value'] < 1.00]



def plot_roc(model, y_true, X_test, model_label=None):
    """TODO: Docstring for plot_roc.

    :model: TODO
    :y_true: TODO
    :X_test: TODO
    :model_label: TODO
    :returns: TODO

    """
    class_pred = model.predict_proba(X_test)[:1]
    false_positive_rates, true_positive_rates, _ = roc_curve(y_true, class_pred)
    store_auc = auc(false_positive_rates, true_positive_rate)

    if model_label is not None:
        tmp_label = f'{model_label}: {round(store_auc, 3)}'
    else:
        tmp_label = None
    plt.plot(false_positive_rates, true_positive_rates, label=tmp_label)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

# Funcion obtenida del auto aprendizaje
def weighting_schedule(voting_ensemble, X_train, X_test, y_train, y_test, weights_dict, plot_scheme=True, plot_performance=True):
    """TODO: Docstring for weighting_schedule.

    :voting_ensemble: TODO
    :X_train: TODO
    :X_test: TODO
    :y_train: TODO
    :y_test: TODO
    :weights_dict: TODO
    :plot_scheme: TODO
    :plot_performance: TODO
    :returns: TODO

    """

    def weight_scheme():
        """TODO: Docstring for weight_scheme.
        :returns: TODO

        """
        weights = pd.DataFrame(weights_dict)
        weights['model'] = [i[0] for i in voting_ensemble.estimators]
        weights = weights.set_index('model')
        sns.heatmap(weights, annot=True, cmap='Blues', cbar=False)
        plt.title('Esquema de Ponderación')

    def weight_performance():
        """TODO: Docstring for weight_performance.
        :returns: TODO

        """

        n_scheme = len(weights_dict)
        f1_metrics, accuracy = [], []
        f1_metrics_train, accuracy_train = [], []

        for i in weights_dict:
            model = voting_ensemble.set_params(weights=weights_dict[i]).fit(X_train, y_train)
            tmp_model_yhat = model.predict(X_test)
            tmp_model_yhat_train = model.predict(X_train)
            f1_metrics.append(f1_score(y_test, tmp_model_yhat).round(3))
            f1_metrics_train.append(f1_score(y_train, tmp_model_yhat_train).round(3))
            accuracy.append(accuracy_score(y_test, tmp_model_yhat).round(3))
            accuracy_train.append(accuracy_score(y_train, tmp_model_yhat_train).round(3))
        plt.plot(range(n_scheme), accuracy, 'o', color='tomato', alpha=.5, label='Exactitud-Test')
        plt.plot(range(n_scheme), f1_metrics, 'x', color='tomato', alpha=.5, label='F1-Test')
        plt.plot(range(n_scheme), accuracy_train, 'o', color='dodgerblue', alpha=.5, label='Exactitud-Train')
        plt.plot(range(n_scheme), f1_metrics_train, 'x', color='dodgerblue', alpha=.5, label='F1-Train')
        plt.xticks(ticks=range(n_scheme), labels=list(weights_dict.keys()), rotation=90)
        plt.title('Desempeño en Train/Test')
        plt.legend(loc='center left', bbox_to_anchor=(1, .5))


    if plot_scheme is True and plot_performance is True:
        plt.subplot(1, 2, 1)
        weight_scheme()
        plt.subplot(1, 2, 2)
        weight_performance()

    else:
        if plot_scheme is True:
            weight_scheme()
        elif plot_performance is True:
            weight_performance()

def committee_voting(voting_ensemble, X_train, X_test, y_train, y_test):
    """TODO: Docstring for committee_voting.

    :voting_ensemble: TODO
    :returns: TODO

    """
    # iniciar dataframe vacio para guardar valores
    individual_preds = pd.DataFrame()
    # preservamos la lista de tuplas
    voting_estimators = voting_ensemble.estimators
    # para cada iterador en la lista de tuplas
    for i in voting_estimators:
        # generamos la estimación específica
        individual_preds[i[0]] = i[1].fit(X_train, y_train).predict(X_test)
    # extraemos los votos individuales de cada clasificador
    individual_preds['votes_n'] = individual_preds.loc[:, voting_estimators[0][0]:voting_estimators[-1][0]].apply(np.sum, axis=1)
    # generamos la predicción del ensamble heterogéneo
    individual_preds['Majority'] = voting_ensemble.set_params(weights=None).predict(X_test)

    # iniciamos un contenedor vacío
    tmp_holder = pd.DataFrame()
    # buscamos el cruce entre cada predicción existente a nivel de modelo
    for i in np.unique(individual_preds['votes_n']):
        # y la predicción a nivel de comité
        for j in np.unique(individual_preds['Majority']):
            # separamos los casos que cumplan con ambas condiciones
            tmp_subset = individual_preds[np.logical_and(
                individual_preds['votes_n'] == i,
                individual_preds['Majority'] == j
            )]
            # extraemos la cantidad de casos existentes
            tmp_rows_n = tmp_subset.shape[0]
            # Si la cantidad de casos existentes es mayor a cero
            if tmp_rows_n > 0:
                # registramos la importancia del clasificador RESPECTO A LA CANTIDAD DE CASOS EXISTENTES.
                tmp_holder[f'Votes: {i} / Class: {j}'] = round(tmp_subset.apply(sum) / tmp_rows_n, 3)
    # transpose
    tmp_holder = tmp_holder.T
    # Eliminamos columnas redundantes del dataframe
    tmp_holder = tmp_holder.drop(columns=['votes_n', 'Majority'])
    # visualizamos la matriz resultante
    sns.heatmap(tmp_holder, annot=True, cmap='coolwarm_r', cbar=False)

def annotated_barplot(variable):
    """TODO: Docstring for annotated_barplot.

    :variable: TODO
    :returns: TODO

    """
    # extraemos la frecuencia de ocurrencia 
    tmp_values = variable.value_counts('%')
    # graficamos y preservamos los atributos del gráfico
    tmp_ax = tmp_values.plot(kind='bar')
    # para cada patch en el gráfico
    for index, patch in enumerate(tmp_ax.patches):
        # anotamos la frecuencia porcentual
        tmp_ax.annotate(tmp_values[index].round(3),
                        # al centro de la barra y arriba
                        xy=(patch.get_x() + .125, patch.get_height() + 0.01),
                        # inferimos el color de cada barra
                        color=patch.get_facecolor())