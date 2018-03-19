# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:03:07 2018

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

def imprime_textos(mapeoElementosCercanos):
    """Muestra los textos por pantalla"""
    contador = 1
    for elem in mapeoElementosCercanos:
        print("Los 10 elementos más cercanos al centro ",contador)
        print("")
        for e in elem:
            print(e)
            print("")
        contador += 1

def mapeo_textos(elementosCentros,bagOfWords):
    """Obtiene las palabras para cada vectorCount"""
    mapeoElementosCercanos = []  
    for elcs in elementosCentros:
        mapeoElementosCercanosActual = []
        for elementoCentro in elcs:
        
            elemento = []
            #print("-----------------------------------")
            contador = 0
            for e in elementoCentro:
                #print(e)
                palabra = bagOfWords[contador]
                if e != 0:
                    elemento.append(palabra)
                
                contador += 1
            mapeoElementosCercanosActual.append(elemento)
        mapeoElementosCercanos.append(mapeoElementosCercanosActual)
    return mapeoElementosCercanos

def obtiene_textos_mas_cercanos_centros(datos,n_centros, n_elementos_mas_cercanos):
    
    elementosCentros = []
    # Para el número de clusters que hemos definido, obtenemos los 10 textos más cernanos al centro
    for cont in range(n_centros): 
        d = kmeans.transform(datosN_train)[:, cont]
        # Nos quedamos con los indices de los 10 elementos más cercanos de cada centro
        ind = np.argsort(d)[::-1][:n_elementos_mas_cercanos]
        
        #print("Los 10 elementos más cercanos al centro ",cont)
        
        elementosActual = []
        
        for elem in ind:
            #print(datosN_train[elem])
            elementosActual.append(datosN_train[elem])
            
        elementosCentros.append(elementosActual)
    return elementosCentros

def obten_datos_corpus(datos):
    corpus = []
    
    for elem in datos[0:90]:
        
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
        
    
    
    # Pasamos a lista de strings
    textosCorpus = []
    for textoLista in corpus:
        texto = ''.join(str(e) + ' ' for e in textoLista)
        texto = texto.rstrip()
        textosCorpus.append(texto)
    return textosCorpus

cats = ['comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware', 'comp.windows.x', 'sci.space' ]
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

pprint(list(newsgroups_train.target_names))

# Comando que sirve para descargar las dependencias de nltk
#nltk.download()


textosCorpus = obten_datos_corpus(newsgroups_train.data)
# Vectorizamos los elementos del corpus
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(textosCorpus)
vectorsArray = vectors.toarray().astype(int)

# Imprimimos la bolsa de palabras para saber qué palabra es cada posición del array

bagOfWords = vectorizer.get_feature_names() 
#print("La bolsa de palabras es:")
#print(bagOfWords)

#Normalizamos los datos entrenamiento
#normalizador = StandardScaler().fit(vectorsArray) # Se ajusta el modelo al conjunto de entrenamiento
#datosN_vectores = normalizador.transform(vectorsArray)

datosN_train, datosN_test = train_test_split(vectorsArray, test_size = 0.25)

# Realizamos el KMedias
kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

kmeans.fit(datosN_train) # Equivalente a Entrena


#print(kmeans.cluster_centers_)

# Obtenemos los elementos mas cercanos a los centros
elementosCentros = obtiene_textos_mas_cercanos_centros(datosN_train,2,10)
# Obtenemos las palabras del texto de la bolsa de palabras para cada vector
mapeoElementosCercanos = mapeo_textos(elementosCentros,bagOfWords)
# Imprimimos el contenido de los textos
imprime_textos(mapeoElementosCercanos)