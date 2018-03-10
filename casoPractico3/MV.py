# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 11:23:54 2018

@author: Ruben
"""

# -*- coding: utf-8 -*-
import votos
import random
import copy
from random import shuffle
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import informacionDigitData
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
        imprimeGrafica(pesosW[2], 'Epochs', 'Verosimilitud')
        
        print("Los pesos obtenidos son: " + str(self.pesosFinales))
        return pesosW
    
    # Devuelve la probabilidad de pertenecer a la clase 1. No se usa en el perceptrón.
    def clasifica_prob(self,ej):
        res = clasifica_probAux(ej,self.pesosFinales,self.norm)
        
        print("La probabilidad de que el ejemplo pertenezca a la clase 1 es: " + str(res))

        return res
    
    def clasifica(self,ej):
        clasificacion = clasificaAux(self.pesosFinales,ej,self.clases,self.norm)
        
        print("El valor de clasificacion es: " + str(clasificacion))
        
        return clasificacion
    
    def evalua(self,prueba,clasesPrueba):
        rendimiento = evaluaAux(self.pesosFinales,prueba,self.clases,clasesPrueba,self.norm)
        
        print("El rendimiento es: " + str(rendimiento) + "\n" + "\n")
        
        return rendimiento 
    
    def oneVsRest(self,entr,clas_entr,n_epochs,ejemplo,rateInicial=0.1,pesos_iniciales=None,rate_decay=False):
        listaPesosClasesOneRest = [] 
        
        clasesCopia = copy.deepcopy(self.clases)
        
        for elem in clasesCopia:
            
            entrenamientoClasesCopia = copy.deepcopy(clas_entr)
            numeroClase = clasesCopia.index(elem)
            
            for idx, item in enumerate(clas_entr):
                if item == elem:
                    entrenamientoClasesCopia[idx] = numeroClase
                    # Asignamos una clase que no exista por ejemplo el 10000
                else:
                    entrenamientoClasesCopia[idx] = 10000
            # Llamamos al metodo entrena para cada una de las clases
            #Cambiarr clas_entr por entrenamientoClasesCopia
            #print(clas_entr)
            self.clases = [numeroClase,10000]
            listaPesos = self.entrena(entr,entrenamientoClasesCopia,n_epochs,rateInicial,pesos_iniciales,rate_decay)
            listaPesosClasesOneRest.append(listaPesos[0])
            
        # Ahora nos quedamos con la clasificacion que nos dee una mayor probabilidad
        
        indiceMaximo = 0
        probabilidadMaxima = 1
        for idx, pesos in enumerate(listaPesosClasesOneRest):
            probabilidad = clasifica_probAux(ejemplo,pesos,self.norm)
            
            if probabilidad <= probabilidadMaxima:
                indiceMaximo = idx
                probabilidadMaxima = probabilidad
        self.clases = clasesCopia
        claseElegida = self.clases[indiceMaximo]
        
        print("El valor de clasificacion para One VS Rest es: " + str(claseElegida))
        return claseElegida
        
def clasifica_probAux(ej,pesosFinales,norm):
    suma = 0
    # Añadimos X0 = 1 al ejemplo
    ejemploCopia = [1] + ej
    
    if norm == True:
        ejemploCopia = normalizaEntrenamiento(ejemploCopia)
    
    contador = 0
    while contador < len(pesosFinales):
        wi = pesosFinales[contador]
        xi = ejemploCopia[contador]
        suma = suma + (wi*xi)
        
        contador += 1
        
    res = sigma(suma)
    #print(str(res))
    #res = 1 - res
        
    
    return res
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
    #print("suma ", suma)   
    
    res = sigma(suma)
    
    
    if res < 0.5:
        clasificacion = clases[0]
        
    else:
        clasificacion = clases[1]
        
    return clasificacion

def entrenaAux(pesosW,entr,clas_entr,n_epochs,rate,clases,rateDecay,norm):
    """Funcion de entrenamiento"""
    erroresGrafica = []
    verosimilitudes = []
    
    #print("len:"  +str(len(entr)))
    #indicesRestantes = list(range(len(entr)))
    #print(str(indicesRestantes))
    
    
    
    pesosIteracion = copy.deepcopy(pesosW)
    
    rateActual = rate
    contadorNumEpochs = 0
    while contadorNumEpochs < n_epochs:
        indicesRestantes = list(range(len(entr)))
        pesosIteracion = np.zeros((len(entr[0]) +1,), dtype=int)
        verosimilitud = 0.0
        while len(indicesRestantes) > 0:
            indice = random.choice(indicesRestantes)
            #print("random:" + str(indice))
            # Añadimos X0 = 1 al ejemplo
            ejemploAdd = [1] + entr[indice]
            #print("pesos ", pesosW)
            res = actualizaPesosEjemplo(pesosW,ejemploAdd,rateActual,clases,clas_entr,indice)
            
            pesosEjemplo = res[0]
            verosimilitud += res[1]
            pesosIteracion = np.sum([pesosIteracion, pesosEjemplo], axis=0)
            #print("pesosW: ", pesosW)
            indicesRestantes.remove(indice)
        contadorNumEpochs += 1
        
        #Disminuimos el rate si nos indican rateDecay = 1
        if rateDecay == True:
            rateActual = rate + (2/(calculaRaiz(contadorNumEpochs**2,3)))
            
        multiplicacion = np.multiply(rate, pesosIteracion)
        
        #res = np.sum([pesosIteracion, multiplicacion], axis=0) 
        
        pesosW = np.sum([pesosW, multiplicacion], axis=0) 
        #print("pesos " , pesosW)  
        rendimiento = evaluaAux(pesosW,entr,clases,clas_entr,norm)
        
        #print("RENDIMIENTO PRUEBA: " +str(rendimiento))
        
        erroresGrafica.append(1-rendimiento)
        verosimilitudes.append(verosimilitud)
        
    return pesosW,erroresGrafica,verosimilitudes

    
def sigma(x):
    """Funcion sigma"""
    try:
        resultado = 1/(1 + math.exp(-x))
    except OverflowError:
        resultado = 1
        
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
    '''wi = wi + η *sum*((y - o)*Xi)'''
    pesosActualizados=[]
    verosimilitudEjemplo = 0.0
    
    clasificacionEjemplo = listaClasesEntrenamiento[indiceEjemplo]
    #y = diccionarioClases[clasificacionEjemplo]
    y = clases.index(clasificacionEjemplo)
    
    W = np.array(listaPesosW)
    X = np.array(ejemplo)
        
    o = sigma(sum(W*X))
        
    
    longitudEjemplo = len(ejemplo)
    contador = 0
    while contador < longitudEjemplo:
        Xi = ejemplo[contador]
      
        WiFinal = (y - o) * Xi
        pesosActualizados.append(WiFinal)
        
        Wi = listaPesosW[contador]
         
        
        # Calculamos la verosimilitud
        WixXi = Wi * Xi
        try:
            exponencialNegativa = math.exp(-1 * WixXi)
        except OverflowError:
            exponencialNegativa = 1
            
        try:
            exponencialPositiva =  math.exp(WixXi)
        except OverflowError:
            exponencialPositiva = 1
        
        
        verosimilitudEjemplo -= math.log(1 + exponencialNegativa) - math.log(1 + exponencialPositiva)  
        
        contador += 1
        
    return pesosActualizados,verosimilitudEjemplo

def calculaRaiz(x,raiz):
    """Metodo para calcular raices"""
    result = x**(1.0/float(raiz))
    
    return result

def imprimeGrafica(valores,xlabel,ylabel):
    """Grafica para imprimir los errores"""
    plt.plot(range(1,len(valores)+1),valores,marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

print("-----------------------------")
print("Votos")
clasificador1 = clasificador(votos.votos_clases,False)
clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,10,rateInicial=0.1,rate_decay=True)
clasificador1.clasifica([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
clasificador1.evalua(votos.votos_test,votos.votos_test_clas)
clasificador1.clasifica_prob([-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0])
print("-----------------------------")


print("-----------------------------")
print("Digitos")
clasificador2 = clasificador(informacionDigitData.clases,False)
clasificador2.oneVsRest(informacionDigitData.trainingNumbers,informacionDigitData.trainingLabels,10,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],rateInicial=0.1,pesos_iniciales=None,rate_decay=True)
clasificador2.evalua(informacionDigitData.testNumbers,informacionDigitData.testLabels)


print("-----------------------------")
print("Numeros aleatorios")
datosAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,10,200,separables=True)
datosTestAleatorios = generacionDatosAleatorios.generaDatosAleatorios(1,10,200,separables=True)

clasificador3 = clasificador(datosAleatorios[2],False)
clasificador3.oneVsRest(datosAleatorios[0],datosAleatorios[1],1000,[1, -1, 0, 1, -1, 2, -1, -2, 1, 3],rateInicial=0.1,pesos_iniciales=None,rate_decay=True)

print("-----------------------------")