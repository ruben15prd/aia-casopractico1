# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:51:38 2018

@author: Ruben
"""
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#news = pd.read_csv("newsCorpora.csv", error_bad_lines=False)



#print(news.head())

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
    
    
