# -*- coding: utf-8 -*-

"""
Created on Wed Mar 14 12:51:38 2018

@author: Ruben
"""
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import nltk

def aplica_stop_words_stemming(datos):
    """Obtiene datos del corpus aplicando stemming y eliminando stop words"""
    res = []
    
    for elem in datos:
        
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

opiniones_procesadas = aplica_stop_words_stemming(opiniones)

# Parámetros TfidfVectorizer
# ngram_range: Número de ngrams mínimos y máximos a ser extraídos
# stop_words: Elimina las stop words
# smooth_idf: Suaviza los pesos idf
# use_idf: Usa idf
# sublinear_tf: Aplica sublinear tf scaling
# binary: Si es verdadero, todos los recuentos de términos distintos de cero se establecen en 1. Esto no significa que los resultados tendrán solo valores de 0/1, solo que el término tf en tf-idf es binario. (Establezca idf y normalización en False para obtener 0/1 salidas).


#Parámetros MultinomialNB
# alpha: Parámetro de suavizado aditivo de Laplace

# Hay que indeicarle el tipo de stem a usar y stop words
pipeline = Pipeline([('tfidf', TfidfVectorizer()), ('clf', MultinomialNB())])
parameters = {  
'tfidf__ngram_range': [(1,3),(1,4),(2,3)],  
#'tfidf__smooth_idf': (True, False),  
#'tfidf__use_idf': (True, False),  
#'tfidf__sublinear_tf': (True, False),  
#'tfidf__binary': (True, False),  
'tfidf__min_df': (0.1,0.5),  
'tfidf__max_df': (0.6,0.9),  
'clf__alpha': [0.5,1.0]
}  

grid_search = GridSearchCV(pipeline, parameters, n_jobs=1, verbose=3)
grid_search.fit(opiniones_procesadas, clasificaciones) 

best_parameters = grid_search.best_estimator_.get_params()  
print()
print("Los mejores parámetros son: ")
print()
print(best_parameters)
print()
pprint(grid_search.grid_scores_)
print()


