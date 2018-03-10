# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#Clasificadores
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier



def representacion_grafica (datos, caracteristicas, objetivo, clases, c1, c2):
    
    for tipo,marca,color in zip(range(len(clases)), "soD", "rgb"):
        
        plt.scatter(datos[objetivo == tipo,c1],
                    datos[objetivo == tipo,c2],
                    marker=marca, c=color)
        
    plt.xlabel(caracteristicas[c1])
    plt.ylabel(caracteristicas[c2])
    plt.legend(clases)
    plt.show()



# Datos y clases de iris
iris = load_iris()
datos_iris, clases_iris = iris.data, iris.target

nombre_columnas, nombre_clases = iris.feature_names, iris.target_names
#representacion_grafica(datos_iris, nombre_columnas, clases_iris, nombre_clases, 0, 1)



# Separacion de datos scikit-learn
datos_train, datos_test, clases_train, clases_test = train_test_split(datos_iris, clases_iris, test_size = 0.25)
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
print("***********************************************\n"
      + "********************  KNN  ********************\n"
      + "***********************************************")
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# Dado un conjunto de entrenamiento, devolver la categoría mayoritaria en los k
# ejemplos mas cercanos al ejemplo que se quiere clasificar.
# DISTANCIAS:
#   euclidea: cada dimension mide propiedades similares.
#   manhatan: cada dimension mide distintas propiedades.
# k = 5 si la clasificacion es binaria.
# Parametros:
#   n_neighbors -> 7 vecinos.
#   weights --> los vecinos mas cercanos tendran mas peso.
#   p -> distancia euclidea.
#   n_jobs -> numero de hilos para ejecucion.
knn = KNeighborsClassifier(n_neighbors=7, weights='distance', p=2, n_jobs=3)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
knn.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaKNN = knn.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn.predict_proba(datosN_test)
print("probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn.score(datosN_test, clases_test) 
print("rendimiento knn: ", rendimientoKNN)


 
print("\n\n***********************************************\n"
      + "*******************  SGDC  ********************\n"
      + "***********************************************")       
#http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html
# Parametros:
#   loss --> funcion de error que se trata de minimizar.
#       Valores:
#           hinge --> clasificador vectores de soporte SVC.
#           log --> regresion logistica.
#           perceptron.
#   penalty.
#       Valores:
#           l2 --> regularizador para modelos lineales SVM.
#           l1 y elasticnet --> aportan menos densidad al modelo (seleccion de caracteristicas).
#   alpha --> importancia de la regularizacion. Para valores grandes, menos sobreajusta y modelo mas simple.
#   learning_rate --> tasa de aprendizaje.
#       Valores: constant, optimal, invscaling.
#   eta0 --> double inicial para el ratio anterior, por defecto es 0.0, cunado toma los valores constant o invscaling.
#   power_t --> exponente de la inversa usada en invscaling.
sgdc = SGDClassifier(loss='hinge', penalty='l2', alpha=0.0001, learning_rate='optimal', n_jobs=3)
sgdc.fit(datosN_train, clases_train) # Equivalente a Entrena

clasificaSGDC = sgdc.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
print("clasifica SGDC: ", clasificaSGDC)

rendimientoSGDC = sgdc.score(datosN_test, clases_test) 
print("rendimiento SGDC: ", rendimientoSGDC)
"""