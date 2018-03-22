# -*- coding: utf-8 -*-
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

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
import math
import copy



clases =["deportes", "politica", "sociedad"] 



titularesDeportes = []
titularesPolitica = []
titularesSociedad = []
titularesPrueba = []
clasificacionesPruebaOld = [] # strings que se han de modificar antes de usarse
clasificacionesPrueba = [] # clasificaciones correctas de los titulares de prueba

# Saco los datos de los archivos txt y los almaceno en variables
[ [ [ titularesDeportes.append(line[:-1]) ] if line[-1]=='\n' else titularesDeportes.append(line) ] for line in open("deportes.txt", 'r', encoding="utf8") ]
[ [ [ titularesPolitica.append(line[:-1]) ] if line[-1]=='\n' else titularesPolitica.append(line) ] for line in open("politica.txt", 'r', encoding="utf8") ]
[ [ [ titularesSociedad.append(line[:-1]) ] if line[-1]=='\n' else titularesSociedad.append(line) ] for line in open("sociedad.txt", 'r', encoding="utf8") ]
[ [ [ titularesPrueba.append(line[:-1]) ] if line[-1]=='\n' else titularesPrueba.append(line) ] for line in open("prueba.txt", 'r', encoding="utf8") ]
[ [ [ clasificacionesPruebaOld.append(line[:-1]) ] if line[-1]=='\n' else clasificacionesPruebaOld.append(line) ] for line in open("prueba_clasificacion.txt", 'r', encoding="utf8") ]

titularesDeportes = titularesDeportes[0].split(". ")
titularesPolitica = titularesPolitica[0].split(". ")
titularesSociedad = titularesSociedad[0].split(". ")
titularesPrueba = titularesPrueba[0].split(". ")
clasificacionesPruebaOld = clasificacionesPruebaOld[0].split(". ")

# Modifico la lista de clasificadores de los titulares de prueba para poder usarlos
[[ clasificacionesPrueba.append(elemento[1:]) if elemento[0][0] == "\ufeff" else clasificacionesPrueba.append(elemento) ] for elemento in clasificacionesPruebaOld ]

print("\n", len(titularesDeportes) + len(titularesPolitica) + len(titularesSociedad) + len(titularesPrueba), "TITULARES:")
print("tamaño titulares deportes: ", len(titularesDeportes))
print("tamaño titulares politica: ", len(titularesPolitica))
print("tamaño titulares sociedad: ", len(titularesSociedad))
print("tamaño titulares prueba: ", len(titularesPrueba))
print("tamaño clasificaciones prueba: ", len(clasificacionesPrueba))



def aplica_stop_words_stemming(datos):
   """Obtiene datos de los titulares aplicando stemming y eliminando stop words"""
   noticias = []
   
   for elem in datos:
       #Eliminamos caracteres especiales
       table = str.maketrans('', '', string.punctuation)
       stripped = [w.translate(table) for w in elem]
   
       # Comprobamos que no sean caracteres especiales y pasamos las palabras a minusculas
       filtrado = [i for i in word_tokenize(elem.lower()) if i not in stripped] 
       
       # Quitamos los caracteres que no son alfabeticos
       words = [word for word in filtrado if word.isalpha()]
       # Filtramos stop words(Palabras no relevantes)
       stop_words = set(stopwords.words('spanish'))
       words = [w for w in words if not w in stop_words]
       # Hacemos stemming
       porter = PorterStemmer()
       stemmed = [porter.stem(word) for word in words]
       
       noticias.append(stemmed)
       
   # Pasamos a lista de strings
   textosNoticias = []
   for textoLista in noticias:
       texto = ''.join(str(e) + ' ' for e in textoLista)
       texto = texto.rstrip()
       textosNoticias.append(texto)
       
   return textosNoticias


titularesDeportes = aplica_stop_words_stemming(titularesDeportes)
titularesPolitica = aplica_stop_words_stemming(titularesPolitica)
titularesSociedad = aplica_stop_words_stemming(titularesSociedad)
titularesPruebaOriginal = copy.deepcopy(titularesPrueba) # Para mostrar el titular original en el resultado
titularesPrueba = aplica_stop_words_stemming(titularesPrueba)
#print(titularesDeportes)



def entrena (titularesDeportes, titularesPolitica, titularesSociedad):
    """Función que realiza el entrenamiento con los tres conjuntos de datos (deportes, politica y sociedad)"""
    dic_palabras_deportes = {}
    dic_palabras_politica = {}
    dic_palabras_sociedad = {}
    total_palabras = []

    # Se crea un diccionario de cada clase con las apariciones de las palabras
    for noticia in titularesDeportes:
        
        for palabra in noticia.split(" "):
            
            if palabra not in dic_palabras_deportes:
                dic_palabras_deportes[palabra] = 1
            else:
                dic_palabras_deportes[palabra] += 1
                
            
            if palabra not in total_palabras:
                total_palabras.append(palabra)
             
                
    for noticia in titularesPolitica:
        
        for palabra in noticia.split(" "):
            
            if palabra not in dic_palabras_politica:
                dic_palabras_politica[palabra] = 1
            else:
                dic_palabras_politica[palabra] += 1
            
            if palabra not in total_palabras:
                total_palabras.append(palabra)


    for noticia in titularesSociedad:
        
        for palabra in noticia.split(" "):
            
            if palabra not in dic_palabras_sociedad:
                dic_palabras_sociedad[palabra] = 1
            else:
                dic_palabras_sociedad[palabra] += 1
            
            if palabra not in total_palabras:
                total_palabras.append(palabra)
            
            
    #print ("diccionario deportes: ", dic_palabras_deportes)
    #print ("diccionario politica: ", dic_palabras_politica)
    #print ("diccionario sociedad: ", dic_palabras_sociedad)

    return [dic_palabras_deportes, dic_palabras_politica, dic_palabras_sociedad, total_palabras]



"""
P(t|c) -> Probabilidad de que aparezca el termino t en la clase c
T c,t -> Numero de veces que aparece el termino t en la clase c
k = 1 -> Para suavizar la funcion
T c,s -> Numero de veces que la palabra s aparece en la clase c. s pertenece a V, el cual es un conjunto con todas las palabras del vocabulario.
|V| -> Numero total de valores del diccionario en cuestion (longitud del diccionario con el total de claves distintas)
"""
def prob_t_aparezca_en_c(termino, clase, diccionarioPalabrasC, total_palabras, k):
    """Probabilidad de que un termino 't' aparezca en el diccionario de la clase 'c'"""
    # P(t|c) = (Tc,t + k) / (sumatorio(Tc,s) + k*|V|) --> El sumatorio es para todas las palabras del vocabulario.
    termino = aplica_stop_words_stemming( [termino] )
    termino = termino[0]
    #print("termino: ", termino)
    veces_aparicion_palabra = 0
    
    if termino in diccionarioPalabrasC:
        veces_aparicion_palabra = diccionarioPalabrasC[termino] # Tc,t
    
    #print("veces aparicion palabra: ", veces_aparicion_palabra)
    total_palabras_clase = 0 # Tc,s
    
    if clase == "deportes":
        
        for elemento in dic_palabras_deportes:
            total_palabras_clase += dic_palabras_deportes[elemento]
        
        
    if clase == "politica":
        
        for elemento in dic_palabras_politica:
            total_palabras_clase += dic_palabras_politica[elemento]
            
        
    if clase == "sociedad":
        
        for elemento in dic_palabras_sociedad:
            total_palabras_clase += dic_palabras_sociedad[elemento]
            
    
    # Probabilidad resultado
    return ( veces_aparicion_palabra + k ) / ( total_palabras_clase + (k * len(total_palabras)) )
    
    

"""print ("yedder en deportes: ", prob_t_aparezca_en_c("Messi", "deportes", dic_palabras_deportes, 1))
print ("yedder en politica: ", prob_t_aparezca_en_c("Messi", "politica", dic_palabras_politica, 1))
print ("yedder en sociedad: ", prob_t_aparezca_en_c("Messi", "sociedad", dic_palabras_sociedad, 1))
print ("inmigrantes en deportes: ", prob_t_aparezca_en_c("inmigrantes", "deportes", dic_palabras_deportes, 1))
print ("inmigrantes en politica: ", prob_t_aparezca_en_c("inmigrantes", "politica", dic_palabras_politica, 1))
print ("inmigrantes en sociedad: ", prob_t_aparezca_en_c("inmigrantes", "sociedad", dic_palabras_sociedad, 1))
print ("alemán en deportes: ", prob_t_aparezca_en_c("alemán", "deportes", dic_palabras_deportes, 1))
print ("alemán en politica: ", prob_t_aparezca_en_c("alemán", "politica", dic_palabras_politica, 1))
print ("alemán en sociedad: ", prob_t_aparezca_en_c("alemán", "sociedad", dic_palabras_sociedad, 1))"""



def clase_mas_probable(titular, dic_palabras_deportes, dic_palabras_politica, dic_palabras_sociedad, total_palabras, k):
    """Se obtiene la clase del diccionario en el que es más probable que aparezca el titular en cuestión"""
    
    probabilidad_total_deportes = 0.0
    probabilidad_total_politica = 0.0
    probabilidad_total_sociedad = 0.0
    
    for termino in titular.split(" "):
        # P(t|c)
        termino_en_deportes = math.log(prob_t_aparezca_en_c(termino, "deportes", dic_palabras_deportes, total_palabras, k))
        termino_en_politica = math.log(prob_t_aparezca_en_c(termino, "politica", dic_palabras_politica, total_palabras, k))
        termino_en_sociedad = math.log(prob_t_aparezca_en_c(termino, "sociedad", dic_palabras_sociedad, total_palabras, k))
        
        probabilidad_total_deportes += termino_en_deportes
        probabilidad_total_politica += termino_en_politica
        probabilidad_total_sociedad += termino_en_sociedad
    
    # P(c) = Nc/N -> probabilidad de que el titular pertenezca a la clase c
    prob_c_deportes = len(titularesDeportes) / (len(titularesDeportes) + len(titularesPolitica) + len(titularesSociedad))
    prob_c_politica = len(titularesPolitica) / (len(titularesDeportes) + len(titularesPolitica) + len(titularesSociedad))
    prob_c_sociedad = len(titularesSociedad) / (len(titularesDeportes) + len(titularesPolitica) + len(titularesSociedad))
    
    # cnb = argmax[ logP(c) + sumatorio(logP(t|c)) ]
    probabilidad_final_deportes = math.log(prob_c_deportes) + probabilidad_total_deportes
    probabilidad_final_politica = math.log(prob_c_politica) + probabilidad_total_politica
    probabilidad_final_sociedad = math.log(prob_c_sociedad) + probabilidad_total_sociedad

    # Se obtiene la clase de la probabilidad máxima
    lista_prob_clases = np.array( [probabilidad_final_deportes, probabilidad_final_politica, probabilidad_final_sociedad] )
    indice = np.argsort(lista_prob_clases)[::-1]
    clase = clases[indice[0]]
        
    return clase
                    


def clasifica (titularesPrueba, k):
    """Función que asigna una clase a un titular nuevo"""
    
    predicciones = []
    
    for titular in titularesPrueba:
        #print("\ntitular original: ", titularesPruebaOriginal[ titularesPrueba.index(titular) ])
        prediccion = clase_mas_probable(titular, dic_palabras_deportes, dic_palabras_politica, dic_palabras_sociedad, total_palabras, k)
        predicciones.append(prediccion)
        #print("clase predicha: ", prediccion)
    
    return predicciones



# clasificacion contiene las clases predichas del conjunto de prueba
def rendimiento (clasificacion, titularesPrueba, clasificacionesPrueba):
    """Función que mide el rendimiento del modelo"""
    
    aciertos = 0
    cont = 0
    
    for prediccion in clasificacion:
        if prediccion == clasificacionesPrueba[ cont ]:
            aciertos += 1
        
        """print("\nprediccion: ", prediccion)
        print("clasificacion: ", clasificacionesPrueba[ cont ])
        print("aciertos:", aciertos)"""
            
        cont += 1
    
    #print (aciertos / len(titularesPrueba))
    return aciertos / len(titularesPrueba)



"""  EJECUCIÓN  """
entrenamiento = entrena(titularesDeportes, titularesPolitica, titularesSociedad)
dic_palabras_deportes = entrenamiento[0]
dic_palabras_politica = entrenamiento[1]
dic_palabras_sociedad = entrenamiento[2]
total_palabras = entrenamiento[3]

# Siendo k = 0.2
clasificacion = clasifica(titularesPrueba, 0.2)
rend = rendimiento(clasificacion, titularesPrueba, clasificacionesPrueba)
print("\n***********************************************")
print ("El rendimiento es del", round(rend*100, 2) , "% cuando k = 0.2")
print("***********************************************")

# Siendo k = 0.55
clasificacion = clasifica(titularesPrueba, 0.55)
rend = rendimiento(clasificacion, titularesPrueba, clasificacionesPrueba)
print("\n***********************************************")
print ("El rendimiento es del", round(rend*100, 2) , "% cuando k = 0.55")
print("***********************************************")

# Siendo k = 1
clasificacion = clasifica(titularesPrueba, 1)
rend = rendimiento(clasificacion, titularesPrueba, clasificacionesPrueba)
print("\n***********************************************")
print ("El rendimiento es del", round(rend*100, 2) , "% cuando k = 1")
print("***********************************************")

# Siendo k = 2
clasificacion = clasifica(titularesPrueba, 2)
rend = rendimiento(clasificacion, titularesPrueba, clasificacionesPrueba)
print("\n***********************************************")
print ("El rendimiento es del", round(rend*100, 2) , "% cuando k = 2")
print("***********************************************")

# Siendo k = 3
clasificacion = clasifica(titularesPrueba, 3)
rend = rendimiento(clasificacion, titularesPrueba, clasificacionesPrueba)
print("\n***********************************************")
print ("El rendimiento es del", round(rend*100, 2) , "% cuando k = 3")
print("***********************************************")