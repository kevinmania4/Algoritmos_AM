# -*- coding: utf-8 -*-
"""RandomForest-Wine

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iHG5Rw55szQZaCSCpqN-RBRNHlpkaZ7A
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#Importando metricas para evaluacion
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
'exec(%matplotlib inline)'

from sklearn.datasets import load_wine

##DATA WINE
wine = datasets.load_wine()
df=pd.DataFrame(wine['data'])
# print(wine)

# # print the label
# print(wine.target_names)

# # print the names of the features
# print(wine.feature_names)

# 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 
# 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 
# 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline'

# Creando un DataFrame
import pandas as pd
data=pd.DataFrame({
    'alcohol':wine.data[:,0],
    'malic_acid':wine.data[:,1],
    'ash':wine.data[:,2],
    'alcalinity_of_ash':wine.data[:,3],
    'magnesium':wine.data[:,4],
    'total_phenols':wine.data[:,5],
    'flavanoids':wine.data[:,6],
    'nonflavanoid_phenols':wine.data[:,7],
    'proanthocyanins':wine.data[:,8],
    'color_intensity':wine.data[:,9],
    'hue':wine.data[:,10],
    'od280/od315_of_diluted_wines':wine.data[:,11],
    'proline':wine.data[:,12],
    'target_names':wine.target
})
data.head()
#VARIABLES DEPENDIENTES
X=data[['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']]  # Features

# VARIABLES INDEPENDIENTES
y=data['target_names']  # Labels


# ##VARIABLES INDEPENDIENTES
# X = np.array(wine['data'])

# ##VARIABLES DEPENDIENTES
# y = np.array(wine['target'])

# Entrenamiento y Prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12) # 70% training and 30% test
print('Son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0], X_test.shape[0])) 

#Importar Modelo Random Forest 
from sklearn.ensemble import RandomForestClassifier

#Crear un Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Entrenamiento del modelo usando los conjuntos de datos
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

from sklearn import metrics

print("Matriz de Confusion: \n",metrics.confusion_matrix(y_test, y_pred))
print("Precisión: ",metrics.precision_score(y_test, y_pred, average=None))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Recall: ",metrics.recall_score(y_test, y_pred , average=None))
print("F1: ",metrics.f1_score(y_test, y_pred, average=None))