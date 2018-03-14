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

cats = ['comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware', 'comp.windows.x', 'sci.space' ]
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

pprint(list(newsgroups_train.target_names))

# Comando que sirve para descargar las dependencias de nltk
#nltk.download()


corpus = []

for elem in newsgroups_train.data[0:90]:
    
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
    

# Vectorizamos los elementos del corpus
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(textosCorpus)
vectorsArray = vectors.toarray().astype(int)

#Normalizamos los datos entrenamiento
#normalizador = StandardScaler().fit(vectorsArray) # Se ajusta el modelo al conjunto de entrenamiento
#datosN_vectores = normalizador.transform(vectorsArray)

datosN_train, datosN_test = train_test_split(vectorsArray, test_size = 0.25)

# Realizamos el KMedias
kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

kmeans.fit(datosN_train) # Equivalente a Entrena


#print(kmeans.cluster_centers_)

for cont in range(2): 
    d = kmeans.transform(datosN_train)[:, cont]
    # Nos quedamos con los indices de los 10 elementos más cercanos de cada centro
    ind = np.argsort(d)[::-1][:10]
    
    print("Los 10 elementos más cercanos al centro ",cont)
    
    [print(datosN_train[elem]) for elem in ind]


