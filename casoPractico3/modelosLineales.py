# -*- coding: utf-8 -*-


class clasificador:
    def __init__(self,clases,norm=False): # norm = valor_columna_ejemplo-media_columna/desv. tipica
        pass
    
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,pesos_iniciales=None,rate_decay=False):
        pass
    
    # Devuelve la probabilidad de pertenecer a la clase 1. No se usa en el perceptrón.
    def clasifica_prob(self,ej):
        pass
    
    def clasifica(self,ej):
        pass