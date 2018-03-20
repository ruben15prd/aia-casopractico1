# -*- coding: utf-8 -*-

"""
Created on Wed Mar 14 12:51:38 2018

@author: Ruben
"""
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score

def aplica_stop_words_stemming(datos):
    """Obtiene datos del corpus aplicando stemming y eliminando stop words"""
    corpus = []
    
    for elem in datos:
        #print("---------------------")
        #print(elem)
        #Eliminamos caracteres especiales
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in elem]

        # Comprobamos que no sean caracteres especiales y pasamos las palabras a minusculas
        filtrado = [i for i in word_tokenize(elem.lower()) if i not in stripped] 
        
        # Quitamos los caracteres que no son alfabeticos
        words = [word for word in filtrado if word.isalpha()]
        # Filtramos stop words(Palabras no relevantes)
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        # Hacemos stemming
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in words]
        
        #print(stemmed)
        corpus.append(stemmed)
    
    return corpus

def obten_datos(nombre_fichero):
    """Obtenemos datos del fichero"""
    opiniones = []
    clasificaciones = []
    
    for line in open(nombre_fichero, 'r', encoding="utf8"):
        split = line.rsplit(',', 1)
        
        
        opinion = split[0]
        clase = split[1]
        
        opiniones.append(opinion)
        clasificaciones.append(clase)
   
    #Eliminamos la cabecera
    opiniones.pop(0)
    clasificaciones.pop(0)
    return opiniones,clasificaciones

# Obtenemos los datos
opiniones,clasificaciones = obten_datos("movie_data.csv")

# Aplicamos stop words y stemming
#opiniones_procesadas = aplica_stop_words_stemming(opiniones[0:100])

# Vectorizamos

# Parámetros TfidfVectorizer
# ngram_range: Número de ngrams mínimos y máximos a ser extraídos
# stop_words: Elimina las stop words
# smooth_idf: Suaviza los pesos idf
# use_idf: Usa idf
# sublinear_tf: Aplica sublinear tf scaling
# binary: Si es verdadero, todos los recuentos de términos distintos de cero se establecen en 1. Esto no significa que los resultados tendrán solo valores de 0/1, solo que el término tf en tf-idf es binario. (Establezca idf y normalización en False para obtener 0/1 salidas).





vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english', smooth_idf=True, use_idf=True, sublinear_tf=True, binary=False)

vectorizerFit = vectorizer.fit(opiniones[0:100])
vectors = vectorizer.transform(opiniones[0:100])

vectorsArray = vectors.toarray().astype(int)

#Separamos los datos
datos_train, datos_test, clases_train, clases_test = train_test_split(vectorsArray, clasificaciones[0:100], test_size = 0.25)

#Parámetros MultinomialNB
# alpha: Parámetro de suavizado aditivo de Laplace
clasificador = MultinomialNB(alpha=1.0)
clasificador.fit(datos_train,clases_train)

predicciones = clasificador.predict(datos_test)

# Comparamos los valores de clasificacion del conjunto de test, con los valores predichos por BinomialNB para el conjunto de test
print("Rendimiento: ")
print(metrics.accuracy_score(clases_test,predicciones))
print("Precisión, exhaustividad y media armónica: ")
print(metrics.classification_report(clases_test,predicciones))
print("Matriz de confusión: ")  #resumen de los aciertos y errores en la clasificación de un conjunto de instancias
print(metrics.confusion_matrix(clases_test,predicciones))

