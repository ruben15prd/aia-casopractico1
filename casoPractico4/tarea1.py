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

cats = ['comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware', 'comp.windows.x', 'sci.space' ]
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

pprint(list(newsgroups_train.target_names))

# Comando que sirve para descargar las dependencias de nltk
#nltk.download()


corpus = []


for elem in newsgroups_train.data:
    print("------")
    
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
    
    print(stemmed)
    corpus.append(stemmed)
    
    

print("Fuera del bucle")
# Vectorizamos los elementos del corpus
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(corpus)


#Normalizamos los datos entrenamiento
normalizador = StandardScaler().fit(vectors) # Se ajusta el modelo al conjunto de entrenamiento
datosN_vectores = normalizador.transform(vectors)

datosN_train, datosN_test = train_test_split(datosN_vectores, test_size = 0.25)

# Realizamos el KMedias
kmeans = KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')


kmeans.fit(datosN_train) # Equivalente a Entrena

# Obtenemos el rendimiento
rendimientoKMeans = kmeans.score(datosN_train) 
print("Rendimiento KMeans: ", rendimientoKMeans) 


