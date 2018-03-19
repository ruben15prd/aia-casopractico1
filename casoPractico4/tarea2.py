# -*- coding: utf-8 -*-

"""
Created on Wed Mar 14 12:51:38 2018

@author: Ruben
"""
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#news = pd.read_csv("newsCorpora.csv", error_bad_lines=False)



#print(news.head())
"""
noticias = []

try:
    for line in open("newsCorpora.csv", 'r'):
        columnas = line.split('\t')
        
        noticia = []
        titular = columnas[1]
        clase = columnas[4]
        
        noticia.append(titular)
        noticia.append(clase)
        
        noticias.append(noticia)
except:
    print("Error")
"""    

titularesDeportes = []
titularesPolitica = []
titularesSociedad = []

# Saco los datos de los archivos txt y los almaceno en variables
[ [ [ titularesDeportes.append(line[:-1]) ] if line[-1]=='\n' else titularesDeportes.append(line) ] for line in open("deportes.txt", 'r', encoding="utf8") ]
[ [ [ titularesPolitica.append(line[:-1]) ] if line[-1]=='\n' else titularesPolitica.append(line) ] for line in open("politica.txt", 'r', encoding="utf8") ]
[ [ [ titularesSociedad.append(line[:-1]) ] if line[-1]=='\n' else titularesSociedad.append(line) ] for line in open("sociedad.txt", 'r', encoding="utf8") ]

titularesDeportes = titularesDeportes[0].split(". ")
titularesPolitica = titularesPolitica[0].split(". ")
titularesSociedad = titularesSociedad[0].split(". ")
print("\n\n", len(titularesSociedad))
print("\n\n", titularesSociedad[3])

