# -*- coding: utf-8 -*-
import votos
import random
import copy
from random import shuffle
import random
import numpy as np
import matplotlib.pyplot as plt
import generacionDatosAleatorios

class clasificador:
    def __init__(self,clases,norm=False): # norm = valor_columna_ejemplo-media_columna/desv. tipica
        self.clases = clases
        self.norm = norm
        self.pesosFinales = None
    
    def entrena(self,entr,clas_entr,n_epochs,rateInicial=0.1,pesos_iniciales=None,rate_decay=False):
        pesosW = []
        
        if self.norm == True:
            entr = normalizaEntrenamiento(entr)
        
        if pesos_iniciales == None:
            pesosW = generaListaPesosAleatoriosW(len(entr[0]) +1,-1.0,1.0)
        else:
            pesosW = pesos_iniciales
            
        pesosW = entrenaAux(pesosW,entr,clas_entr,n_epochs,rateInicial,self.clases,rate_decay,self.norm)
        
        
        self.pesosFinales = pesosW[0]
        
        imprimeGrafica(pesosW[1], 'Epochs', 'Porcentaje de errores')
        
        print("Los pesos obtenidos son: " + str(self.pesosFinales))
        return pesosW
    
    # Devuelve la probabilidad de pertenecer a la clase 1. No se usa en el perceptrón.
    def clasifica_prob(self,ej):
        pass
    
    def clasifica(self,ej):
        clasificacion = clasificaAux(self.pesosFinales,ej,self.clases,self.norm)
        
        print("El valor de clasificacion es: " + str(clasificacion))
        
        return clasificacion
    
    def evalua(self,prueba,clasesPrueba):
        rendimiento = evaluaAux(self.pesosFinales,prueba,self.clases,clasesPrueba,self.norm)
        
        print("El rendimiento es: " + str(rendimiento) + "\n" + "\n")
        return rendimiento 
    
def normalizaEntrenamiento(entr):
    """Funcion usada para normalizar el conjunto de entrenamiento"""
    
    #Calculamos las medias
    medias = np.mean(entr, axis=0)
    #Calculamos las desviaciones tipicas
    desviacionTipica = np.std(entr, axis=0)
    
    #Restamos las medias al conjunto de entrenamiento
    conjuntoResta = np.subtract(entr, medias)
    #Dividimos por las desviaciones tipicas
    conjuntoDivision = np.divide(conjuntoResta, desviacionTipica)
    
    return conjuntoDivision.tolist()


def evaluaAux(pesos,prueba,clases,clasesEntrenamiento,norm):
    """Metodo para evaluar un conjunto de prueba"""
    aciertos = 0
    numTotal = len(prueba)
    contadorEjemplo = 0
    for p in prueba:
        #print("p: " + str(p))
        clasificacion = clasificaAux(pesos,p,clases,norm)
        #print("clase predecida: " + str(clasificacion))
        #print("clase original: " + str(clasesEntrenamiento[contadorEjemplo]))
        if clasificacion == clasesEntrenamiento[contadorEjemplo]:
            aciertos = aciertos + 1
        contadorEjemplo += 1
    rendimiento = aciertos/numTotal
    
    return rendimiento
    
       
def clasificaAux(pesosFinales,ejemplo,clases,norm):
    """Funcion de clasificacion auxiliar"""
    suma = 0
    # Añadimos X0 = 1 al ejemplo
    ejemploCopia = [1] + ejemplo
    
    if norm == True:
        ejemploCopia = normalizaEntrenamiento(ejemploCopia)
    
    contador = 0
    while contador < len(pesosFinales):
        wi = pesosFinales[contador]
        xi = ejemploCopia[contador]
        suma = suma + (wi*xi)
        
        contador += 1
        
    res = umbral(suma)
    
    #print(str(clases))
    #Quitar esto, usar las clases del clasificador
    clasificacion = clases[res]
    return clasificacion

def entrenaAux(pesosW,entr,clas_entr,n_epochs,rate,clases,rateDecay,norm):
    """Funcion de entrenamiento"""
    
    #print("len:"  +str(len(entr)))
    erroresGrafica = []
    #print(str(indicesRestantes))
    rateActual = rate
    contadorNumEpochs = 0
    while contadorNumEpochs < n_epochs:
        indicesRestantes = list(range(len(entr)))
        while len(indicesRestantes) > 0:
            indice = random.choice(indicesRestantes)
            #print("random:" + str(indice))
            # Añadimos X0 = 1 al ejemplo
            ejemploAdd = [1] + entr[indice]
                
            pesosW = actualizaPesosEjemplo(pesosW,ejemploAdd,rateActual,clases,clas_entr,indice)
            
            indicesRestantes.remove(indice)
        contadorNumEpochs += 1
        
        #Disminuimos el rate si nos indican rateDecay = 1
        if rateDecay == True:
            rateActual = rate + (2/(calculaRaiz(contadorNumEpochs**2,3)))
        
        rendimiento = evaluaAux(pesosW,entr,clases,clas_entr,norm)
        erroresGrafica.append(1-rendimiento)
        
    return pesosW,erroresGrafica

    
def umbral(x):
    """Funcion umbral"""
    resultado = 0
    if x >= 0:
        resultado = 1
    else:
        resultado = 0
        
    return resultado

def generaListaPesosAleatoriosW(longitudAGenerar,limiteInferior,limiteSuperior):
    """Genera la lista W de pesos aleatorios entre 2 limites"""
    W = []
    
    while longitudAGenerar > 0:
        aleatorio = random.uniform(limiteInferior, limiteSuperior)
        
        W.append(aleatorio)
        longitudAGenerar -= 1
    return W


def actualizaPesosEjemplo(listaPesosW,ejemplo,rate,clases,listaClasesEntrenamiento,indiceEjemplo):
    """Actualiza la lista de pesos W, dado un ejemplo(recordar que este ejemplo tiene que incorporar X0)"""
    '''wi = wi + ηxi(y − o)'''
    pesosActualizados=[]
    
    clasificacionEjemplo = listaClasesEntrenamiento[indiceEjemplo]
    #y = diccionarioClases[clasificacionEjemplo]
    y = clases.index(clasificacionEjemplo)
    
    W = np.array(listaPesosW)
    X = np.array(ejemplo)
        
    o = umbral(sum(W*X))
        
    
    longitudEjemplo = len(ejemplo)
    contador = 0
    while contador < longitudEjemplo:
        Xi = ejemplo[contador]
        Wi = listaPesosW[contador]
      
        WiFinal = Wi + ((rate*Xi)*(y - o))
        pesosActualizados.append(WiFinal)
            
        contador += 1
        
    return pesosActualizados

def calculaRaiz(x,raiz):
    result = x**(1.0/float(raiz))
    
    return result

def imprimeGrafica(valores,xlabel,ylabel):
    """Grafica para imprimir los errores"""
    plt.plot(range(1,len(valores)+1),valores,marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


"""
Bateria de tests:
    Normalización: True
    N_epochs: 50-80-100
    rateInicial = 0.2-0.05
    rate_decay = True

Para reducir el número de combinaciones hemos realizado algunas pruebas previas con la normalización
y el rate_decay. Se obtiene mejor resultado con ambos a True aunque a veces la mejora no es muy notable.

Para las pruebas con el conjunto aleatorio se realizarán con conjuntos no separables, ya que para los separables
con un número grande de épocas se podría fácilmente encontrar un hiperplano que nos delimite los valores de
clasificación. Por lo tanto, con un número elevado de épocas se obtendría un alto valor de rendimiento o incluso
un 100%.

Para el conjunto de dígitos sólo hemos hecho una prueba con los siguientes parámetros:
    Normalización: True(Para votos y dígitos), False para el conjunto de números aleatorios
    N_epochs: 10
    rateInicial = 0.05
    rate_decay = True
    
Para el conjunto de dígitos aleatorios se generan 200 ejemplos (150 entrenamiento, 50 test)

"""
print("----------------------------------")
print("Prueba 1 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,50,rateInicial=0.2,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)

print("----------------------------------")
print("Prueba 2 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,80,rateInicial=0.2,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)

print("----------------------------------")
print("Prueba 3 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,100,rateInicial=0.2,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)

print("----------------------------------")
print("Prueba 4 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,50,rateInicial=0.05,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)

print("----------------------------------")
print("Prueba 5 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,80,rateInicial=0.05,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)

print("----------------------------------")
print("Prueba 6 - Votos:")
clasificador1 = clasificador(votos.votos_clases,True)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,100,rateInicial=0.05,pesos_iniciales=None,rate_decay=False)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)


print("----------------------------------")


print("-----------------------------")
print("Prueba 1 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,50,rateInicial=0.2,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)

print("-----------------------------")
print("Prueba 2 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,80,rateInicial=0.2,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)


print("-----------------------------")
print("Prueba 3 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,100,rateInicial=0.2,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)


print("-----------------------------")
print("Prueba 4 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,50,rateInicial=0.05,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)

print("-----------------------------")
print("Prueba 5 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,80,rateInicial=0.05,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)

print("-----------------------------")
print("Prueba 6 - Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,5,200,separables=False)
datosAleatoriosEntrenamiento = datosAleatorios[0][0:150]
datosAleatoriosClasesEntrenamiento = datosAleatorios[1][0:150]
datosAleatoriosTest = datosAleatorios[0][150:]
datosAleatoriosClasesTest = datosAleatorios[1][150:]

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.entrena(datosAleatoriosEntrenamiento,datosAleatoriosClasesEntrenamiento,100,rateInicial=0.05,rate_decay=True)
clasificador3.clasifica([-1,1,-1,1,1])
clasificador3.evalua(datosAleatoriosTest,datosAleatoriosClasesTest)

