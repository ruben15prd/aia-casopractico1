# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:00:44 2018

@author: Ruben
"""


def obtenNumeros(nombreFichero):
    """Metodo que obtiene cada numero de los ficheros. Cada linea del numero se
    concatena a la anterior y cada lista sublista contendra un numero completo"""
    mapeos = [' ','+','#']     
    ficheroCodificado = []
            
    #Extraemos informacion de los digitos escritos
    for line in open(nombreFichero, 'r'):
        #print("-------------------")
        #print(str(line))
        lineaCodificada = []
        for l in line:
            if l in [' ','+','#']:
                indiceConversion = mapeos.index(l)
                lineaCodificada.append(indiceConversion)
        
        ficheroCodificado.append(lineaCodificada)
                
        
    #print(str(ficheroCodificado))  
    ficheroFinal = []
    actual = []
    for elem in ficheroCodificado:
        
        a = checkEqual(elem)
        if a == False:
            #print(elem)
            actual = actual + elem 
            
        else:
            if len(actual) > 0:
                ficheroFinal.append(actual)
            actual = []
    
    return ficheroFinal

def obtenClases(nombreFichero):
    """Metodo que obtiene los valores de clasificacion"""
    labels = []
    
    for line in open(nombreFichero, 'r'):
        line = line.strip('\n')
        if line != "":
            labels.append(line)
            
    return labels
        
def checkEqual(iterator):
    """Metodo que comprueba si todos los elementos de una lista son iguales"""
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)
    
#Extraemos los valores de clasificacion para el conjunto de entrenamiento
trainingLabels = obtenClases("traininglabels")
#Extraemos los valores de clasificacion para el conjunto de validacion     
validationLabels = obtenClases("validationlabels")
#Extraemos los valores de clasificacion para el conjunto de test 
testLabels = obtenClases("testlabels")
  
#Extraemos los numeros del conjunto de entrenamiento
trainingNumbers = obtenNumeros("trainingimages")
#Extraemos los numeros del conjunto de validacion
validationNumbers = obtenNumeros("validationimages")
#Extraemos los numeros del conjunto de entrenamiento
testNumbers = obtenNumeros("testimages")

"""
print("Training images: " + str(trainingNumbers))
print("Training labels: " + str(trainingLabels))
print("Validation images: " + str(validationNumbers))
print("Validation labels: " + str(validationLabels))
print("Test images: " + str(testNumbers))
print("Test labels: " + str(testLabels))
"""


