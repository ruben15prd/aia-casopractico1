# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_breast_cancer
import informacionDigitData
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#Clasificadores
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier



def representacion_grafica (datos, caracteristicas, objetivo, clases, c1, c2):
    
    for tipo,marca,color in zip(range(len(clases)), "soD", "rgb"):
        
        plt.scatter(datos[objetivo == tipo,c1],
                    datos[objetivo == tipo,c2],
                    marker=marca, c=color)
        
    plt.xlabel(caracteristicas[c1])
    plt.ylabel(caracteristicas[c2])
    plt.legend(clases)
    plt.show()



# Datos y clases de cancer de mama
cancer = load_breast_cancer()
datos_cancer, clases_cancer = cancer.data, cancer.target
nombre_columnas, nombre_clases = cancer.feature_names, cancer.target_names


# Representacion grafica de los datos de cáncer de mama
representacion_grafica(datos_cancer, nombre_columnas, clases_cancer, nombre_clases, 2, 14)
representacion_grafica(datos_cancer, nombre_columnas, clases_cancer, nombre_clases, 14, 1)


# Separacion de datos
#datos_train, datos_test, clases_train, clases_test = train_test_split(datos_iris, clases_iris, test_size = 0.25)
datos_train, datos_test, clases_train, clases_test = train_test_split(datos_cancer, clases_cancer, test_size = 0.25)
#print("ENTRENAMIENTO:\n", datos_train)
#print("CLASES ENTRENAMIENTO:\n", clases_train)



# Datos de los digitos (informacionDigitData)
datos_digit_train = informacionDigitData.trainingNumbers
datos_digit_test = informacionDigitData.testNumbers
clases_digit_train = informacionDigitData.trainingLabels
clases_digit_test = informacionDigitData.testLabels


# Conversion en arrays de numpy
datos_trainNP = np.array(datos_digit_train)
datos_testNP = np.array(datos_digit_test)
clases_trainNP = np.array(clases_digit_train)
clases_testNP = np.array(clases_digit_test)



print("*********************************************************\n"
      + "**************************  KNN  ************************\n"
      + "*********************************************************")

"""
Dado un conjunto de entrenamiento, devolver la categoría mayoritaria en los k
ejemplos mas cercanos al ejemplo que se quiere clasificar.
DISTANCIAS:
   euclidea: cada dimension mide propiedades similares.
   manhatan: cada dimension mide distintas propiedades.
 k = 5 si la clasificacion es binaria.
 Parametros:
   n_neighbors -> 7 vecinos.
   weights --> el valor distance supone que los vecinos mas cercanos tendran mas peso.
   algoritm --> algoritmo usado para calcular los vecinos mas cercanos.
       brute --> se usa una búsqueda de fuerza bruta.
       auto --> intenta decidir el algoritmo mas apropiado en funcion de los valores pasados a fit. 
   p -> distancia euclidea si es 2, si es 1 es manhattan.
   n_jobs -> numero de hilos para ejecucion.
"""

print("----------------------------------")
print("PRUEBA 1 - Cáncer de mama:")
knn1 = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm = 'brute', p=2, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
knn1.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaKNN = knn1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 cancer clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn1.predict_proba(datosN_test)
#print("P1 cancer probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn1.score(datosN_test, clases_test)
print("P1 cancer rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 95%


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
knn2 = KNeighborsClassifier(n_neighbors=3, weights='distance', algorithm = 'auto', p=1, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
knn2.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaKNN = knn2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 cancer clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn2.predict_proba(datosN_test)
#print("P2 cancer probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn2.score(datosN_test, clases_test) 
print("P2 cancer rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 98%


print("----------------------------------")
print("PRUEBA 3 - Cáncer de mama:")
knn3 = KNeighborsClassifier(n_neighbors=10, weights='uniform', algorithm = 'brute', p=31, n_jobs=1)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
knn3.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaKNN = knn3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 cancer clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn3.predict_proba(datosN_test)
#print("P3 cancer probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn3.score(datosN_test, clases_test) 
print("P3 cancer rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 90%

# Viendo los resultados obtenidos, se puede decir que el knn da los mejores resultados cuando los vecinos cercanos
# tienen más peso que los demás, cuando el algoritmo usado para el calculo de dichos vecinos dependa de los valores
# pasados a fit y cuando la distancia sea manhatan. El rendimiento es del 98%.


print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
knn5 = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm = 'brute', p=2, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
knn5.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaKNN = knn5.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn5.predict_proba(datosN_testNP)
#print("P1 digitos probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn5.score(datosN_testNP, clases_testNP) 
print("P1 digitos rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 86%


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
knn6 = KNeighborsClassifier(n_neighbors=3, weights='distance', algorithm = 'auto', p=1, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
knn6.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaKNN = knn6.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn6.predict_proba(datosN_testNP)
#print("P2 digitos probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn6.score(datosN_testNP, clases_testNP) 
print("P2 digitos rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 89%


print("----------------------------------")
print("PRUEBA 3 - Dígitos:")
knn6 = KNeighborsClassifier(n_neighbors=10, weights='uniform', algorithm = 'brute', p=31, n_jobs=1)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
knn6.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaKNN = knn6.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 digitos clasifica knn: ", clasificaKNN)
clasificaProbabilidadKNN = knn6.predict_proba(datosN_testNP)
#print("P3 digitos probabilidad clasifica knn:\n", clasificaProbabilidadKNN)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoKNN = knn6.score(datosN_testNP, clases_testNP) 
print("P3 digitos rendimiento knn: ", rendimientoKNN) # EL RENDIMIENTO OBTENIDO ES DEL 61%

# El mayor rendimiento que se obtiene con los digitos es del 89%. En la prueba 3, como es de esperar, al aumentar el
# valor de p aumenta el tiempo de calculo. Hay mejor rendimiento cuando los vecinos mas cercanos tienen mas peso y se
# busca el algoritmo adecuado en función de los valores pasados al entrena.


 
print("\n\n***************************************************************\n"
      + "*******************  SGDC Vectores Soporte ********************\n"
      + "***************************************************************")       

"""
Parametros:
   loss --> funcion de error que se trata de minimizar.
       Valores:
           hinge --> clasificador vectores de soporte SVC.
           log --> regresion logistica.
           perceptron.
   penalty.
       Valores:
           l2 --> regularizador para modelos lineales SVM.
           l1 y elasticnet --> aportan menos densidad al modelo (seleccion de caracteristicas).
   alpha --> importancia de la regularizacion. Para valores grandes, menos sobreajusta y modelo mas simple.
   max_iter -->  número máximo de epochs.
   tol --> criterio de parada. Las iteraciones se detendrán cuando loss > loss anterior - tol
   learning_rate --> tasa de aprendizaje.
       Valores: constant, optimal, invscaling.
   eta0 --> double inicial para el ratio anterior, por defecto es 0.0, cuando toma los valores constant o invscaling.
   power_t --> exponente de la inversa usada en invscaling.
"""

print("----------------------------------")
print("PRUEBA 1 - Cáncer de mama:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l1', alpha=0.9, max_iter=35, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc1.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC1 = sgdc1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 cancer clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_test, clases_test) 
print("P1 cancer rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 62%


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l1', alpha=0.9, max_iter=1000, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc1.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC1 = sgdc1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 cancer clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_test, clases_test) 
print("P2 cancer rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 62%


print("----------------------------------")
print("PRUEBA 3 - Cáncer de mama:")
sgdc1 = SGDClassifier(loss='hinge', penalty='elasticnet', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', eta0=0.8, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc1.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC1 = sgdc1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 cancer clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_test, clases_test) 
print("P3 cancer rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 95%


print("----------------------------------")
print("PRUEBA 4 - Cáncer de mama:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l2', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc1.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC1 = sgdc1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P4 cancer clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_test, clases_test) 
print("P4 cancer rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 97%


print("----------------------------------")
print("PRUEBA 5 - Cáncer de mama:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l2', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', power_t=7, eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc1.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC1 = sgdc1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P5 cancer clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_test, clases_test) 
print("P5 cancer rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 93%

# Se puede observar en las dos primeras pruebas que aumentando el número de iteraciones, el rendimiento no cambia.
# Cuando la penalización y la tasa de aprendizaje toma los valores l2 (regularizador para modelos lineales) e
# invscaling respectivamente, además de eta0=0.2, el rendimiento es del 97%.  Cabe mencionar que si se aumenta en
# exponente de la inversa (power_t) el rendimiento baja. Esto se puede comprobar en la prueba 5.



print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l1', alpha=0.9, max_iter=35, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc1.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc1.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_testNP, clases_testNP) 
print("P1 digitos rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 10%


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
sgdc1 = SGDClassifier(loss='hinge', penalty='elasticnet', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', eta0=0.8, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc1.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc1.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_testNP, clases_testNP) 
print("P2 digitos rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 78%


print("----------------------------------")
print("PRUEBA 3 - Dígitos:")
sgdc1 = SGDClassifier(loss='hinge', penalty='l2', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc1.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc1.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 digitos clasifica SGDC Vectores Soporte: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc1.score(datosN_testNP, clases_testNP) 
print("P3 digitos rendimiento SGDC Vectores Soporte: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 84%

# El rendimiento para los dígitos es peor frente a los datos de cancer de mama, pero aun así se supera el 80% en el
# mejor de los casos, se llega al 84%. El mayor rendimiento se da en el mismo caso que con los datos de cancer, cuando
# la penalización y la tasa de aprendizaje toman los valores l2 e invscaling respectivamente, además de eta0 el valor 0.2.



print("\n\n********************************************************\n"
      + "*******************  SGDC Regresion ********************\n"
      + "********************************************************")       

print("----------------------------------")
print("PRUEBA 1 - Cáncer de mama:")
sgdc2 = SGDClassifier(loss='log', penalty='l1', alpha=0.0001, tol=0.1, learning_rate='constant', eta0=0.1, n_jobs=1)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc2.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC2 = sgdc2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 cancer clasifica SGDC Regresion: ", clasificaSGDC2)

rendimientoSGDC2 = sgdc2.score(datosN_test, clases_test)
print("P1 cancer rendimiento SGDC Regresion: ", rendimientoSGDC2) # EL RENDIMIENTO ES DEL 96%


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
sgdc2 = SGDClassifier(loss='log', penalty='l1', alpha=0.2, max_iter=1000, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc2.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC2 = sgdc2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 cancer clasifica SGDC Regresion: ", clasificaSGDC2)

rendimientoSGDC2 = sgdc2.score(datosN_test, clases_test)
print("P2 cancer rendimiento SGDC Regresion: ", rendimientoSGDC2) # EL RENDIMIENTO ES DEL 88%


print("----------------------------------")
print("PRUEBA 3 - Cáncer de mama:")
sgdc2 = SGDClassifier(loss='log', penalty='l1', alpha=0.9, max_iter=35, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc2.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC2 = sgdc2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 cancer clasifica SGDC Regresion: ", clasificaSGDC2)

rendimientoSGDC2 = sgdc2.score(datosN_test, clases_test)
print("P3 cancer rendimiento SGDC Regresion: ", rendimientoSGDC2) # EL RENDIMIENTO ES DEL 62%


print("----------------------------------")
print("PRUEBA 4 - Cáncer de mama:")
sgdc2 = SGDClassifier(loss='log', penalty='elasticnet', alpha=0.1, max_iter=1000, tol=0.5, learning_rate='invscaling', eta0=0.8, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc2.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC2 = sgdc2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P4 cancer clasifica SGDC Regresion: ", clasificaSGDC2)

rendimientoSGDC2 = sgdc2.score(datosN_test, clases_test)
print("P4 cancer rendimiento SGDC Regresion: ", rendimientoSGDC2) # EL RENDIMIENTO ES DEL 94%


print("----------------------------------")
print("PRUEBA 5 - Cáncer de mama:")
sgdc2 = SGDClassifier(loss='log', penalty='l2', alpha=0.1, max_iter=50, tol=0.5, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc2.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC2 = sgdc2.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P5 cancer clasifica SGDC Regresion: ", clasificaSGDC2)

rendimientoSGDC2 = sgdc2.score(datosN_test, clases_test)
print("P5 cancer rendimiento SGDC Regresion: ", rendimientoSGDC2) # EL RENDIMIENTO ES DEL 95%

# Se puede observar que la primera prueba ha obtenido un 96% de rendimiento con una penalizacion l1 y muy poco
# sobreajuste, tambien con un modelo poco complejo. Con la penalizacion l1, la tasa de aprendizaje optimal y
# un menor sobreajuste se ha obtenido el peor rendimiento, un 62%.


print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
sgdc2 = SGDClassifier(loss='log', penalty='l2', alpha=0.1, max_iter=50, tol=0.5, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc2.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc2.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica SGDC Regresion: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc2.score(datosN_testNP, clases_testNP) 
print("P1 digitos rendimiento SGDC Regresion: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 83%


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
sgdc2 = SGDClassifier(loss='log', penalty='l1', alpha=0.9, max_iter=35, tol=0.5, learning_rate='optimal', n_jobs=3)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc2.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc2.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica SGDC Regresion: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc2.score(datosN_testNP, clases_testNP) 
print("P2 digitos rendimiento SGDC Regresion: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 10%


print("----------------------------------")
print("PRUEBA 3 - Dígitos:")
sgdc2 = SGDClassifier(loss='log', penalty='l1', alpha=0.0001, tol=0.1, learning_rate='constant', eta0=0.1, n_jobs=1)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc2.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC1 = sgdc2.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 digitos clasifica SGDC Regresion: ", clasificaSGDC1)

rendimientoSGDC1 = sgdc2.score(datosN_testNP, clases_testNP) 
print("P3 digitos rendimiento SGDC Regresion: ", rendimientoSGDC1) # EL RENDIMIENTO OBTENIDO ES DEL 79%

# De nuevo, el rendimiento de digitos es menor que el de los datos de cancer de mama, su valor es de algo más del 80%.
# Los valores son muy similares a los de vectores de soporte.



print("\n\n*********************************************************\n"
      + "*******************  SGDC Perceptron ********************\n"
      + "*********************************************************")

print("----------------------------------")
print("PRUEBA 1 - Cáncer de mama:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l1', alpha=0.9, max_iter=50, tol=0.5, learning_rate='constant', eta0=0.5, n_jobs=3) #0.4195804195804196

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc3.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC3 = sgdc3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 cancer clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_test, clases_test)
print("P1 cancer rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 58%


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l1', alpha=0.9, max_iter=60, tol=0.5, learning_rate='constant', eta0=0.5, n_jobs=1)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc3.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC3 = sgdc3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 cancer clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_test, clases_test)
print("P2 cancer rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 58%


print("----------------------------------")
print("PRUEBA 3 - Cáncer de mama:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l1', alpha=0.9, max_iter=1000, tol=0.5, learning_rate='constant', eta0=0.5, n_jobs=1)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc3.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC3 = sgdc3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 cancer clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_test, clases_test)
print("P3 cancer rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 41%


print("----------------------------------")
print("PRUEBA 4 - Cáncer de mama:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l2', alpha=0.0001, tol=0.5, learning_rate='optimal', n_jobs=2)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc3.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC3 = sgdc3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P4 cancer clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_test, clases_test)
print("P4 cancer rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 96%


print("----------------------------------")
print("PRUEBA 5 - Cáncer de mama:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l2', alpha=0.1, max_iter=1000, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
sgdc3.fit(datosN_train, clases_train) # Equivalente a Entrena

datosN_test = normalizador.transform(datos_test)
clasificaSGDC3 = sgdc3.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P5 cancer clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_test, clases_test)
print("P5 cancer rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 97%

# El perceptron obtiene el mejor rendimiento cuando la penalización es l2, la tasa de aprendizaje es invscaling y
# alpha es bajo. El rendimiento baja casi al 40% cuando la penalizacion es l1, la tase de aprensizaje es constante
# y el sobreajuste baja.
# Si no se normaliza el conjunto de test habiendo normalizado el de entrenamiento, el rendimiento esta por debajo del
# 70%.
#n_jobs no afecta al rendimento de las pruebas de SGDC realizadas.


print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l1', alpha=0.9, max_iter=1000, tol=0.5, learning_rate='constant', eta0=0.5, n_jobs=1)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc3.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC3 = sgdc3.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_testNP, clases_testNP)
print("P1 digitos rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 9%


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l2', alpha=0.0001, tol=0.5, learning_rate='optimal', n_jobs=2)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc3.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC3 = sgdc3.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_testNP, clases_testNP)
print("P2 digitos rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 86%


print("----------------------------------")
print("PRUEBA 3 - Dígitos:")
sgdc3 = SGDClassifier(loss='perceptron', penalty='l2', alpha=0.1, max_iter=1000, learning_rate='invscaling', eta0=0.2, n_jobs=4)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
sgdc3.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

datosN_testNP = normalizador.transform(datos_testNP)
clasificaSGDC3 = sgdc3.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 digitos clasifica SGDC Perceptron: ", clasificaSGDC3)

rendimientoSGDC3 = sgdc3.score(datosN_testNP, clases_testNP)
print("P3 digitos rendimiento SGDC Perceptron: ", rendimientoSGDC3) # EL RENDIMEINTO ES DEL 80%

# Estas pruebas siguen la misma tonica que las anteriores, el rendimiento de los datos de digitos es mas bajo, superior al 80%,
# sigue siendo más bajo que el de los datos de cancer de mama. Los valores tomados para el mejor rendimiento son los
# mismos que los tomados para los datos cancer, las dos ultimas pruebas de los datos de cancer daban un rendimiento por encima
# del 95% y en estas uñtimas pruebas superan el 80%.



print("\n\n***************************************************\n"
      + "********************  Árboles  ********************\n"
      + "***************************************************")

"""
criterion: Función que se usará para dividir el nodo. Posibles valores: gini, entropy
splitter: Estrategia que se usara para dividir cada nodo. Posibles valores: best, random
max_depth: Profundidad máxima del árbol
min_samples_split: Tamaño mínimo de ejemplos requeridos para dividir un nodo interno.
min_samples_leaf: Mínimo número de ejemplos requeridos para ser un nodo hoja.
max_features: Número de características que se usan cuando se divide.
"""

print("----------------------------------")
print("PRUEBA 1 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
#print("P1 probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("P1 rendimiento arboles: ", rendimientoArboles)

# En este caso se ha realizado la prueba con los valores por defecto, como se puede apreciar con este conjunto tiene
# un rendimiento superior al 90%.


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='gini', splitter='random', max_depth=None, min_samples_split=60, min_samples_leaf=40, max_features=2)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
#print("P2 probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("P2 rendimiento arboles: ", rendimientoArboles)

# En este caso se ha intentado probando con los valores para ver qué parámetros que hace que empeore mucho el score.
# Usando el splitter de manera aleatoria hará que no se comporte bien al elegir el atributo del nodo. Si a esto le
# sumamos que va a crear hojas cuando aún le quedan muchos elementos, esto hará que la  clasificación sea mucho peor.
# El rendimiento es del 60%.


print("----------------------------------")
print("PRUEBA 3 - Cáncer de mama:")
arboles = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P3 clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_test)
#print("P3 probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_test, clases_test) 
print("P3 rendimiento arboles: ", rendimientoArboles)

# Tras hacer varias pruebas esta es la que ha dado mejor resultado. Usando la entropia como criterio de clasificacion
# y el mejor split se obtiene un rendimiento del 93%.


print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
arboles = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=80, min_samples_split=10, min_samples_leaf=15, max_features=None)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
arboles.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaArboles = arboles.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_testNP)
#print("P1 digitos probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_testNP, clases_testNP) 
print("P1 digitos rendimiento arboles: ", rendimientoArboles)


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
arboles = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
arboles.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaArboles = arboles.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica arboles: ", clasificaArboles)
clasificaProbabilidadArboles = arboles.predict_proba(datosN_testNP)
#print("P2 digitos probabilidad clasifica arboles:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles.score(datosN_testNP, clases_testNP) 
print("P2 digitos rendimiento arboles: ", rendimientoArboles)

# En estas dos pruebas realizadas al conjunto de dígitos se consiguen unos porcentajes cercanos al 65% y al 75%
# respectivamente, más concretamente un 68% y un 73%. Dicho rendimiento es peor que el obtenido con el conjunto
# de datos de cancer.



print("\n\n*********************************************************\n"
      + "********************  Random Forest  ********************\n"
      + "*********************************************************")

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
print("PRUEBA 1 - Cáncer de mama:")
arboles1 = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles1.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles1.predict_proba(datosN_test)
#print("P1 probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles1.score(datosN_test, clases_test) 
print("P1 rendimiento random forest: ", rendimientoArboles)


print("----------------------------------")
print("PRUEBA 2 - Cáncer de mama:")
arboles1 = RandomForestClassifier(n_estimators=80, criterion='entropy', max_depth=55, min_samples_split=25, min_samples_leaf=25, max_features=20)

normalizador = StandardScaler().fit(datos_train) # Se ajusta el modelo al conjunto de entrenamiento
datosN_train = normalizador.transform(datos_train)
arboles1.fit(datosN_train, clases_train) # Equivalente a Entrena

# Metodo clasifica
datosN_test = normalizador.transform(datos_test)
clasificaArboles = arboles1.predict(datosN_test) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles1.predict_proba(datosN_test)
#print("P2 probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles1.score(datosN_test, clases_test) 
print("P2 rendimiento random forest: ", rendimientoArboles)

# Usando indistintamente los dos criterios de decision posibles (gini y entropia), se consiguen rendimientos
# entorno al 95%. La primera prueba tiene un 97% y la segunda un 94%.


print("----------------------------------")
print("PRUEBA 1 - Dígitos:")
arboles1 = RandomForestClassifier(n_estimators=80, criterion='entropy', max_depth=40, min_samples_split=30, min_samples_leaf=30, max_features=20)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
arboles1.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaArboles = arboles1.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P1 digitos clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles1.predict_proba(datosN_testNP)
#print("P1 digitos probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles1.score(datosN_testNP, clases_testNP) 
print("P1 digitos rendimiento random forest: ", rendimientoArboles)


print("----------------------------------")
print("PRUEBA 2 - Dígitos:")
arboles1 = RandomForestClassifier(n_estimators=80, criterion='entropy', max_depth=55, min_samples_split=25, min_samples_leaf=25, max_features=20)

normalizador = StandardScaler().fit(datos_trainNP) # Se ajusta el modelo al conjunto de entrenamiento
datosN_trainNP = normalizador.transform(datos_trainNP)
arboles1.fit(datosN_trainNP, clases_trainNP) # Equivalente a Entrena

# Metodo clasifica
datosN_testNP = normalizador.transform(datos_testNP)
clasificaArboles = arboles1.predict(datosN_testNP) # Se usa el modelo ajustado para predecir la clase de nuevas instancias
#print("P2 digitos clasifica random forest: ", clasificaArboles)
clasificaProbabilidadArboles = arboles1.predict_proba(datosN_testNP)
#print("P2 digitos probabilidad clasifica random forest:\n", clasificaProbabilidadArboles)

# Rendimiento: porcentaje de aciertos sobre el conjunto de test
rendimientoArboles = arboles1.score(datosN_testNP, clases_testNP) 
print("P2 digitos rendimiento random forest: ", rendimientoArboles)

# En el caso de los digitos mediante random forest, con los parámetros anteriores se consigue un 82 y un 83% de rendimiento,
# en las dos pruebas se obtiene un valor menor que el calculado con los datos de cancer.