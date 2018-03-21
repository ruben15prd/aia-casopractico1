# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:03:07 2018

@author: Ruben
"""
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
from sklearn.cluster import KMeans
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def imprime_textos(elementosCercanosCentro):
    """Muestra los textos por pantalla"""

    for elem in elementosCercanosCentro:
        print("----------------------------------------------------")
        print(elem)
    

def obtiene_elementos_mas_cercanos_centro(datos_vectores, datos_originales,n_centro, n_elementos_mas_cercanos):
    """Obtiene los elementos más cercanos a los centros"""
    elementosCentros = []
    # Para el número de clusters que hemos definido, obtenemos los 10 textos más cernanos al centro
    
    d = kmeans.transform(datos_vectores)[:, n_centro]
    #print(d)
    # Nos quedamos con los indices de los 10 elementos más cercanos de cada centro
    ind = np.argsort(d)[::-1][:n_elementos_mas_cercanos]
    #ind = np.argsort(d)[-3:][::-1]
    #print(ind)
    
    for elem in ind:
        #print(datos[elem])
        elementosCentros.append(datos_originales[elem])
        
    return elementosCentros

def aplica_stop_words_stemming(datos):
    """Obtiene datos del corpus aplicando stemming y eliminando stop words"""
    res = []
    
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
        res.append(stemmed)
        
    
    # Pasamos a lista de strings
    textosRes = []
    for textoLista in res:
        texto = ''.join(str(e) + ' ' for e in textoLista)
        texto = texto.rstrip()
        textosRes.append(texto)
    return textosRes

cats = ['comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware', 'comp.windows.x', 'sci.space' ]
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
newsgroups_test = fetch_20newsgroups(subset='test', categories=cats)

pprint(list(newsgroups_train.target_names))

# Comando que sirve para descargar las dependencias de nltk
#nltk.download()

textosCorpus = aplica_stop_words_stemming(newsgroups_train.data)
# Vectorizamos los elementos del corpus
vectorizer = CountVectorizer()

vectorizerFit = vectorizer.fit(textosCorpus)
vectors = vectorizer.transform(textosCorpus)

vectorsArray = vectors.toarray().astype(int)


# Imprimimos la bolsa de palabras para saber qué palabra es cada posición del array

bagOfWords = vectorizer.get_feature_names() 
#print("La bolsa de palabras es:")
#print(bagOfWords)


datosN_train, datosN_test = train_test_split(vectorsArray, test_size = 0.25)

# Realizamos el KMedias
kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

kmeans.fit(datosN_train) # Equivalente a Entrena

# Clasificamos el primer elemento de nuestro conjunto de tests, le aplicamos stop words, stemming y vectorizamos

# Aplicamos stop words y stemming al elemento de nuestro conjunto de tests

textoTest = aplica_stop_words_stemming([newsgroups_test.data[0]])

# Vectorizamos
vectorTest = vectorizer.transform(textoTest)
vectorsTestArray = vectorTest.toarray().astype(int)

# Realizamos predict para ver a que cluster pertenece
predicciones = kmeans.predict(vectorsTestArray)# Obtenemos la prediccion del primer elemento
prediccion = predicciones[0]

print("Las predicciones para los datos de tests son para el clúster: ",prediccion)

#Obtenemos los elementos más cercanos
elementos_mas_cercanos = obtiene_elementos_mas_cercanos_centro(datosN_train,newsgroups_train.data,prediccion, 3)
# Imprimimos los textos más cercanos
imprime_textos(elementos_mas_cercanos)


