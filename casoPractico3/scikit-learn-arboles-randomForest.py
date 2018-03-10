# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#Clasificadores
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


import informacionDigitData



def representacion_grafica (datos, caracteristicas, objetivo, clases, c1, c2):
    
    for tipo,marca,color in zip(range(len(clases)), "soD", "rgb"):
        
        plt.scatter(datos[objetivo == tipo,c1],
                    datos[objetivo == tipo,c2],
                    marker=marca, c=color)
        
    plt.xlabel(caracteristicas[c1])
    plt.ylabel(caracteristicas[c2])
    plt.legend(clases)
    plt.show()



# Datos y clases de cancer
cancer = load_breast_cancer()
datos_cancer, clases_cancer = cancer.data, cancer.target
nombre_columnas, nombre_clases = cancer.feature_names, cancer.target_names
#representacion_grafica(datos_iris, nombre_columnas, clases_iris, nombre_clases, 0, 1)



# Separacion de datos scikit-learn
datos_train, datos_test, clases_train, clases_test = train_test_split(datos_cancer, clases_cancer, test_size = 0.25)
#print("ENTRENAMIENTO:\n", datos_train)
#print("CLASES ENTRENAMIENTO:\n", clases_train)



#Normalizacion de datos
#print("Datos entrenamiento sin normalizar:")
#representacion_grafica(datos_train, nombre_columnas, clases_train, nombre_clases, 0, 1)
#normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
#datosN_train = normalizador.transform(datos_train)
#print("Datos entrenamiento normalizados:")
#representacion_grafica(datosN_train, nombre_columnas, clases_train, nombre_clases, 0, 1)



print("***********************************************\n"
      + "********************  Árboles  ********************\n"
      + "***********************************************")

"""

criterion: Función que se usará para dividir el nodo. Posibles valores: gini, entropy
splitter: Estrategia que se usara para dividir cada nodo. Posibles valores: best, random
max_depth: Profundidad máxima del árbol
min_samples_split: Tamaño mínimo de ejemplos requeridos para dividir un nodo interno.
min_samples_leaf: Mínimo número de ejemplos requeridos para ser un nodo hoja.
max_features: Número de características que se usan cuando se divide.

"""

print("----------------------------------")
print("Prueba 1 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("rendimiento arboles: ", rendimientoArboles)

#En este caso hemos probado con los valores por defecto, como se puede apreciar con este conjunto tiene un rendimiento cercano al 90%


print("----------------------------------")
print("Prueba 2 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='gini', splitter='random', max_depth=None, min_samples_split=60, min_samples_leaf=40, max_features=2)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("rendimiento arboles: ", rendimientoArboles)

# En este caso se ha intentado probando con los valores para ver qué parámetros que hace que empeore mucho el score. Usando el splitter de manera aleatoria hará que no se 
# comporte bien al elegir el atributo del nodo. Si a esto le sumamos que va a crear hojas cuando aún le quedan muchos elementos, esto hará que la 
# clasificación sea mucho peor


print("----------------------------------")
print("Prueba 3 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("rendimiento arboles: ", rendimientoArboles)

# Tras hacer varias pruebas esta es la que nos ha dado mejor resultado

# Extraemos los datos de los numeros

#datos_train = informacionDigitData.trainingNumbers

#datos_numeros, clases_numeros = informacionDigitData.trainingNumbers, informacionDigitData.trainingLabels


datos_train = informacionDigitData.trainingNumbers
datos_test = informacionDigitData.testNumbers
clases_train = informacionDigitData.trainingLabels
clases_test = informacionDigitData.testLabels


#Hay que pasar esto a arrays de numpy

datos_trainNP = np.array(datos_train)
datos_testNP = np.array(datos_test)
clases_trainNP = np.array(clases_train)
clases_testNP = np.array(clases_test)

print("----------------------------------")
print("Prueba 1 - Dígitos:")
arboles = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=80, min_samples_split=10, min_samples_leaf=15, max_features=None)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_trainNP)
arboles.fit(datosN_train, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_testNP)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_testNP) 
print("rendimiento arboles: ", rendimientoArboles)

# En los dígitos se consigue un porcentaje cercano al 65% un rendimiento bastante bajo

print("***********************************************\n"
      + "********************  Random Forest  ********************\n"
      + "***********************************************")


# Datos y clases de cancer
cancer = load_breast_cancer()
datos_cancer, clases_cancer = cancer.data, cancer.target
nombre_columnas, nombre_clases = cancer.feature_names, cancer.target_names
#representacion_grafica(datos_iris, nombre_columnas, clases_iris, nombre_clases, 0, 1)



# Separacion de datos scikit-learn
datos_train, datos_test, clases_train, clases_test = train_test_split(datos_cancer, clases_cancer, test_size = 0.25)
#print("ENTRENAMIENTO:\n", datos_train)
#print("CLASES ENTRENAMIENTO:\n", clases_train)



#Normalizacion de datos
#print("Datos entrenamiento sin normalizar:")
#representacion_grafica(datos_train, nombre_columnas, clases_train, nombre_clases, 0, 1)
#normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
#datosN_train = normalizador.transform(datos_train)
#print("Datos entrenamiento normalizados:")
#representacion_grafica(datosN_train, nombre_columnas, clases_train, nombre_clases, 0, 1)

"""
n_estimators:  Número de árboles
criterion: Función que se usará para dividir el nodo. Posibles valores: gini, entropy
splitter: Estrategia que se usara para dividir cada nodo. Posibles valores: best, random
max_depth: Profundidad máxima del árbol
min_samples_split: Tamaño mínimo de ejemplos requeridos para dividir un nodo interno.
min_samples_leaf: Mínimo número de ejemplos requeridos para ser un nodo hoja.
max_features: Número de características que se usan cuando se divide.

"""

print("----------------------------------")
print("Prueba 1 - Cáncer de mama:")
arboles = RandomForestClassifier(n_estimators=10, criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("rendimiento random forest: ", rendimientoArboles)

#En este caso hemos probado con los valores por defecto, como se puede apreciar con este conjunto tiene un rendimiento cercano al 95%



print("----------------------------------")
print("Prueba 2 - Cáncer de mama:")
arboles = RandomForestClassifier(n_estimators=80, criterion='entropy', max_depth=55, min_samples_split=25, min_samples_leaf=25, max_features=20)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("rendimiento random forest: ", rendimientoArboles)

# Tras hacer varias pruebas esta es la que nos ha dado mejor resultado, consiguiendo un 97% 

# Extraemos los datos de los numeros

#datos_train = informacionDigitData.trainingNumbers

#datos_numeros, clases_numeros = informacionDigitData.trainingNumbers, informacionDigitData.trainingLabels


datos_train = informacionDigitData.trainingNumbers
datos_test = informacionDigitData.testNumbers
clases_train = informacionDigitData.trainingLabels
clases_test = informacionDigitData.testLabels


#Hay que pasar esto a arrays de numpy

datos_trainNP = np.array(datos_train)
datos_testNP = np.array(datos_test)
clases_trainNP = np.array(clases_train)
clases_testNP = np.array(clases_test)

print("----------------------------------")
print("Prueba 1 - Dígitos:")
arboles = RandomForestClassifier(n_estimators=80, criterion='entropy', max_depth=40, min_samples_split=30, min_samples_leaf=30, max_features=20)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_trainNP)
arboles.fit(datosN_train, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_testNP)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("Clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
print("probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_testNP) 
print("rendimiento random forest: ", rendimientoArboles)

# En el caso de los digitos mediante random forest, con los parámetros anteriores se consigue un 82% de rendimiento, como se puede apreciar mejora
# mucho el resultado de decision tree que era de un 62%