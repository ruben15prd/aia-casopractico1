# -*- coding: utf-8 -*-
import votos
import random
import copy
from random import shuffle
import random
import numpy as np

def generacionDatosAleatorios(rango,dimension,tamañoConjunto,separables=True):
    """Funcion que genera datos aleatorios"""
    plano = []
    conjunto = []
    clasesConjunto = []
    porcentajeNoSeparable = 0.1 #Porcentaje cuando queremos que el conjunto sea no separable
    
    
    #Construimos la ecuacion del plano
    for i in range(dimension):
        aleatorio = np.random.randint(-rango, rango)
        plano.append(aleatorio)
    
    
    for j in range(tamañoConjunto):
        elemento = []
        for k in range(dimension):
            aleatorio = np.random.randint(-rango, rango)
            elemento.append(aleatorio)
        conjunto.append(elemento) 
        #Generamos la clase
     
        multiplicacion = np.multiply(plano,elemento)
        suma = np.sum(multiplicacion)
        
        # Si queremos generar un conjunto no separable, tenemos que cambiar
        #con un determinado porcentaje la clase a la clase a la que va asociada
        if separables == False:
            aleatorioNoSeparable = random.random()
            if aleatorioNoSeparable <= porcentajeNoSeparable:
                suma = suma*(-1)
        
        #Si esta por debajo del hiperplano, le adjudicamos la clase 0
        if suma < 0:
            clasesConjunto.append(0)
        #Si esta por encima del hiperplano, le adjudicamos la clase 1
        else:
            clasesConjunto.append(1)
    
    
    return conjunto,clasesConjunto   


#res = generacionDatosAleatorios(3,10,20,False)