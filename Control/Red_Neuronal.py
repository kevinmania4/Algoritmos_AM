from sklearn import datasets
import numpy
from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
##########LIBRERÍAS A UTILIZAR##########
#Se importan la librerias a utilizar
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

##########IMPORTANDO LA DATA##########
import pandas
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris();
wine = datasets.load_wine();

nombres_iris = iris['target_names']
nombres_wine = wine['target_names']

Xi = iris.data[:, :]  # we only take the first two features.
yi = iris.target

##########APLICACIÓN DE ALGORITMOS DE MACHINE LEARNING##########
#Separo la columna con la información de los sobrevivientes
X_traini, X_testi, y_traini, y_testi = train_test_split(Xi, yi, test_size=0.3, random_state=24)


from sklearn.neural_network import MLPClassifier
mlp=MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=500, alpha=0.0001,
                     solver='adam', random_state=21,tol=0.000000001)
#mlp = MLPClassifier(hidden_layer_sizes=(6,6,6,6),solver='lbfgs',max_iter=6000)


mlp.fit(X_traini, y_traini)
y_predi =mlp.predict(X_testi)

'''
from skearn.metrics import classification_report
print(classification_report(y_test,Y_pred))
'''
###Medidas de rendimiento

matrixconfusioni=metrics.confusion_matrix(y_testi, y_predi)
precisioni=metrics.precision_score(y_testi, y_predi, average=None)
accuracyi=metrics.accuracy_score(y_testi, y_predi)
recalli=metrics.recall_score(y_testi, y_predi , average=None)
f1i=metrics.f1_score(y_testi, y_predi, average=None)

print("Medidas de rendimiento ")
print("Matriz de Confusion: \n",matrixconfusioni)
print("Precisión: \n",precisioni)
print("Accuracy:\n",accuracyi)
print("Recall: \n",recalli)
print("F1: \n",f1i)
###########

# import some data to play with
Xw = wine.data[:, :]  # we only take the first two features.
yw = wine.target

##########APLICACIÓN DE ALGORITMOS DE MACHINE LEARNING##########
#Separo la columna con la información de los sobrevivientes
X_trainw, X_testw, y_trainw, y_testw = train_test_split(Xw, yw, test_size=0.3, random_state=24)


from sklearn.neural_network import MLPClassifier
mlp=MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=500, alpha=0.0001,
                     solver='adam', random_state=21,tol=0.000000001)
#mlp = MLPClassifier(hidden_layer_sizes=(6,6,6,6),solver='lbfgs',max_iter=6000)


mlp.fit(X_trainw, y_trainw)
y_predw =mlp.predict(X_testw)
'''
from skearn.metrics import classification_report
print(classification_report(y_test,Y_pred))'''


# print("Medidas de rendimiento ")
matrixconfusionw=metrics.confusion_matrix(y_testw, y_predw)
precisionw=metrics.precision_score(y_testw, y_predw, average=None)
accuracyw=metrics.accuracy_score(y_testw, y_predw)
recallw=metrics.recall_score(y_testw, y_predw , average=None)
f1w=metrics.f1_score(y_testw, y_predw, average=None)
print("Matriz de Confusion: \n",matrixconfusionw)
print("Precisión: \n",precisionw)
print("Accuracy:\n",accuracyw)
print("Recall: \n",recallw)
print("F1: \n",f1w)