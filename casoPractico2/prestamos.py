# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Sat Feb 17 16:59:51 2018

@author: Ruben
"""
# ==================================================
# Conjunto de datos "Concesión de préstamos"
# Aplicaciones de Inteligencia Artificial.
# Máster en Ingeniería Informática
# ==================================================

# Contiene una serie de datos sobre concesión de préstamos en una entidad
# bancaria, en función de:

# * Tipo de empleo: funcionario, contrato laboral, parado o jubilado
# * Productos finacieros contratados en la misma entidad: 0, 1 o más de 2.
# * Propiedades inmobiliarias: 0,1 o más de 2.
# * Número de hijos: 0, 1 o más de 2.
# * Estado civil: soltero, casao, viudo, divorciado. 
# * Ingresos: bajos, medios, altos

atributos=[("Empleo",["parado", "funcionario", "laboral", "jubilado"]),
           ("Productos",["ninguno", "uno", "dos o más"]),
           ("Propiedades",["ninguna", "una", "dos o más"]),
           ("Hijos",["ninguno", "uno", "dos o más"]),
           ("Estado civil",["soltero", "casado","viudo","divorciado"]),
           ("Ingresos", ["bajos","medios","altos"])]           

# El atributo de clasificación indica si se concede o no el préstamo
# solicitado: 

clasificacion='Préstamo'

clases=['conceder','no conceder','estudiar']

# Conjuntos de entrenamiento, validación y prueba

entrenamiento=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','viudo','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','dos o más','soltero','altos','estudiar'],
      ['funcionario','ninguno','dos o más','dos o más','viudo','bajos','estudiar'],
      ['laboral','ninguno','una','dos o más','viudo','altos','conceder']]

entrenamiento2=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','viudo','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','dos o más','soltero','altos','estudiar'],
      ['funcionario','ninguno','dos o más','dos o más','viudo','bajos','estudiar'],
      ['laboral','ninguno','una','dos o más','viudo','altos','conceder'],
      ['funcionario','uno','una','uno','viudo','medios','estudiar'],
      ['parado','dos o más','ninguna','uno','casado','medios','no conceder'],
      ['parado','dos o más','dos o más','uno','divorciado','bajos','estudiar'],
      ['funcionario','dos o más','ninguna','dos o más','divorciado','altos','conceder'],
      ['funcionario','uno','dos o más','dos o más','soltero','altos','conceder'],
      ['parado','ninguno','dos o más','dos o más','divorciado','altos','conceder'],
      ['funcionario','ninguno','ninguna','uno','viudo','altos','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','ninguno','una','uno','soltero','bajos','estudiar'],
      ['funcionario','uno','una','ninguno','divorciado','altos','conceder']]




def aprendizajeArbolesDecision(conjuntoInicio, atributos, funcionClasificacion, cotaMinima=0, cotaMayoria=1):
    #conjuntoActual y atributosRestantes son listas de indices
    conjuntoActual = list(range(len(conjuntoInicio)))
    atributosRestantes = list(range(len(atributos)))
    aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes)

def aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes):

    # Crear parametro para almacenar la clase del nodo anterior y pasarsela al nodo hoja cuando no hay mas elementos, compruebaCasoBase=0
    # Si es caso base se construye un nodo hoja
    print("----------------")
    print("conjuntoActual: " + str(conjuntoActual))
    print("atributosRestantes: " + str(atributosRestantes))
    
    
    if compruebaCasoBase(conjuntoInicio, conjuntoActual, atributosRestantes, cotaMinima, cotaMayoria ) == 1:
        if len(conjuntoActual) == 1:
            nodoHoja1 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                              atributo=None,
                              ramas=None,
                              clase=conjuntoInicio[conjuntoActual[0]][len(conjuntoInicio[conjuntoActual[0]])-1])
            
            distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
            atributo=None
            ramas=None
            clase=conjuntoInicio[conjuntoActual[0]][len(conjuntoInicio[conjuntoActual[0]])-1]
            print ("nodoHoja1:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                   " -clase:" + str(clase))
    
    
    else:
        instanciasClaseMaxima = calculaDistribucion(conjuntoInicio, conjuntoActual)
        claseMaxima = max(instanciasClaseMaxima, key=instanciasClaseMaxima.get)
        
        
        # Si no es caso base se elige el mejor atributo atr(mejor atributo) usando la funcion clasifica(funcionClasificacion), dentro se ponen los distintos sumatorios de Entropia y los otros
        
        indiceMejorAtributo = obtenMejorAtributo(conjuntoInicio, atributos, conjuntoActual, atributosRestantes, funcionClasificacion)
        print("indice: " + str(indiceMejorAtributo))
        #Creamos el conjunto actual de cada una de las ramas
        for valor in atributos[indiceMejorAtributo][1]:
            nuevoConjuntoActual = []
            #print("valor: " + str(valor))
            
            for indice in conjuntoActual:
                #print("fila: " + str(fila))
                datoEntrenamiento = conjuntoInicio[indice]
                if valor == datoEntrenamiento[indiceMejorAtributo]:
                    nuevoConjuntoActual.append(indice)
            
            #print ("conjActual:" + str(nuevoConjuntoActual))
        
            #Creamos los atributos restantes de cada una de las ramas
            
            atribRestantes = atributosRestantes[:]
            atribRestantes.remove(indiceMejorAtributo)
            #del(atribRestantes[indiceMejorAtributo])
        
            #print("atributosDespues:" + str(atributosRestantes) )
            #print("atributosRestantesDespues:" + str(atribRestantes) )
        
            # Se construye un nodo internmedio con distr, atr, ramas{valorAtributo: aprendizajeRecursivo(
            #       conjuntoInicio, atributos, porcentajeMinimo, porcentajeMayoria, nuevoConjuntoActual,
            #       atributosRestantes-atr)}
        
            # No hacer llamadas recursivas sin ejemplos
            if len(nuevoConjuntoActual) > 0:
                nuevoNodo = NodoDT(distr=calculaDistribucion(conjuntoInicio,nuevoConjuntoActual),
                                   atributo=indiceMejorAtributo,
                                   ramas={valor: aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, nuevoConjuntoActual, atribRestantes)},
                                   clase=None)
                
                distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
                atributo=indiceMejorAtributo
                ramas={valor: aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, nuevoConjuntoActual, atribRestantes)}
                clase=None
                print ("nuevoNodo:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                   " -clase:" + str(clase))
            else:#Creo una hoja con la clase anterior
                nodoHoja2 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                                   atributo=None,
                                   ramas=None,
                                   clase=claseMaxima)
                
                distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
                atributo=None
                ramas=None
                clase=claseMaxima
                print ("nodoHoja1:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                   " -clase:" + str(clase))
        
        
    
      
    
    
    #1. Crear un nodo raiz conteniendo el conjunto inicial de entrenamiento D
    #2. REPETIR (hasta que no haya mas candidatos a nodos internos)
        #2.1 SELECCIONAR un nodo candidato a nodo interno
        #2.2 ELEGIR un criterio de decision
        #2.3 Crear los descendientes con los datos del nodo candidato que satisfacen el correspondiente valor del criterio de decision
    #3. ETIQUETAR cada nodo hoja con la clase dominante en los datos de dicho nodo (si no tiene datos, se usa la clase dominante en los datos del nodo padre)
    #4. PODAR nodos para evitar sobreajuste


def compruebaCasoBase(conjuntoInicio, conjuntoActual, atributosRestantes, cotaMinima=0, cotaMayoria=1):
    casoBase = 0
    
    primero = conjuntoInicio[conjuntoActual[0]][len(conjuntoInicio[conjuntoActual[0]])-1]
    #print ("primero: " + primero)
    
    # CASOS BASE:
    #  - Cuando todos los datos son de la misma clase
    for elem in conjuntoActual:
        
        datoEntrenamiento = conjuntoInicio[elem]
        valorClase = datoEntrenamiento[len(datoEntrenamiento) - 1]
        if valorClase == primero:
            casoBase = 1
            #print ("if :"+elem[len(elem)-1])
        else:
            casoBase = 0
            #print ("else :"+elem[len(elem)-1])
            break
    
    #  - Todos los elementos son muy pocos comparados con los que habia al principio
    elemsMin = len(conjuntoActual) / len(conjuntoInicio)
    if elemsMin < cotaMinima:
        casoBase = 1
    
    #  - Cuando la mayoria sean todos de la misma clase
    dicClase = calculaDistribucion(conjuntoInicio, conjuntoActual)
    #print (dicClase)
    
       
    elemsMax = max(dicClase.values()) / len(conjuntoActual)
    #print (elemsMax)
    
    if elemsMax > cotaMayoria:
        casoBase = 1
    
    #CASOS EN LOS QUE SE HAN DE CREAR HOJAS:
    #   Si se queda el conjunto con un ejemplo se devuelve una hoja con la clase mayoritaria
    #   Si el conjunto está vacío se devuelve una hoja con la clase mayoritaria del nodo anterior
    if len(conjuntoActual) <= 1: 
        casoBase = 1
        
    # Si se queda sin atributos
    if len(atributosRestantes) == 0:
        casoBase = 1
    
    return casoBase

def calculaDistribucion(conjuntoInicio, conjuntoActual):
    dicClases = {}
    for e in clases:
        dicClases[e] = 0
    
    for elem1 in conjuntoActual:
        
        datoEntrenamiento = conjuntoInicio[elem1]
        
        valorClase = datoEntrenamiento[len(datoEntrenamiento) - 1]
        dicClases[ valorClase ] += 1
    
    return dicClases

class NodoDT(object):
    def __init__(self,atributo=-1,distr=None,ramas=None,clase=None):
        self.distr=distr # Diccionario con el numero de ejemplos de cada clase
        self.atributo=atributo # Indice del atributo, solo para  nodos internos
        self.ramas=ramas # Diccionario con tantas claves como valores tenga el atributo (valor del atributo: nodo inferior)
        self.clase=clase # Solo para nodos hojas
        
def obtenMejorAtributo(conjuntoInicio, atributos, conjuntoActual, atributosRestantes, funcionClasificacion):
    result = ""
    dic = calculaAtributoValores(conjuntoInicio, atributos, conjuntoActual, atributosRestantes)
    #instanciasClaseMaxima = max(calculaDistribucion(conjuntoInicio, conjuntoActual))
    #print ("iteracion: "+str(dic))  
    # Calcular la impureza del nodo padre y restarla al sumatorio de ni/n * impureza de cada valor del atributo
    # Padre {'conceder': 6, 'no conceder': 2, 'estudiar': 7} --> - 6/15*log2(6/15) - 2/15*log2(2/15) - 7/15*log2(7/15)
        
    #print("antes de error")
    # Se hacen los sumatorios con los valores de cada atributo y quedarnos con el menor para "error"
    #Impureza del padre
    
    
    #print("---------")
    #print("CONJUNTOINICIO: " + str(conjuntoInicio))
    #print("ATRIBUTOSRESTANTES: " + str(atributosRestantes))
    if funcionClasificacion == "error":
        
        #impurezaPadre = 1 - pd/S
        
        distribucionClases = calculaDistribucion(conjuntoInicio,conjuntoActual)
        pdPadre = sorted(distribucionClases.values())[len(distribucionClases) - 1]
        
        
        impurezaPadre = 1 - (pdPadre/len(conjuntoActual))
        
        #print("entra en error")
        tam = len(conjuntoActual)
        indiceAtributoMaximo = 0
        valorErrorMinimo = 1.0
        for elem in atributosRestantes:
            error = 0.00
            #print(str(elem)) 
            #print(str(dic[elem]))
            for elem1 in dic[elem]:
                #print(str(elem1))
                    
                if dic[elem][elem1][0] > 0:
                    pd = dic[elem][elem1][0]
                    si = dic[elem][elem1][1]
                        
                    error += (pd/tam)*(1 - (si/pd))
                      
            #print("atributo nuevo:"+str(error))
            
                
            impurezaTotalAtributo = impurezaPadre - error
            if impurezaTotalAtributo < valorErrorMinimo:
                valorErrorMinimo = error
                indiceAtributoMaximo = elem
            
        #print(indiceAtributoMaximo)
        return indiceAtributoMaximo
                
            
    """elif funcionClasificacion == "gini":
    else funcionClasificacion == "entropia":
    """
    


def calculaAtributoValores(conjuntoInicio, atributos, conjuntoActual, atributosRestantes):
    diccionarioAtributosValores = {}
    contadorPosicion = 0
  
    dicClases = calculaDistribucion(conjuntoInicio, conjuntoActual)
  
    claseMaxima = max(dicClases, key=dicClases.get)
  
    for atr in atributosRestantes:
        listaValoresAtributo = atributos[atr][1]
        dic = {}
      
        for atrVal in listaValoresAtributo:
            dic[atrVal] = [0,0]
      
        diccionarioAtributosValores[atributosRestantes[contadorPosicion]] = dic
        contadorPosicion += 1
    #print(str(diccionarioAtributosValores))
        
    for entrada in conjuntoActual:
        contadorPosicion = 0
        datoEntrenamiento = conjuntoInicio[entrada]
        clase = datoEntrenamiento[len(datoEntrenamiento) - 1]
        #print(str(datoEntrenamiento))
        todosIndices = list(range(len(atributos)))
        a = np.array(todosIndices)
        b = atributosRestantes
        #print("-------")
        #print( str(list(a[b])))
        res= list(a[b])
        
        c = np.array(datoEntrenamiento)
        d = res
        #print("-------")
        #print( str(list(c[d])))
        indicesAObtener = list(c[d])
        
        for elem in indicesAObtener:
        #for elem in datoEntrenamiento[0:len(datoEntrenamiento) - 1]:
        #for elem in atributosRestantes:
            #todosIndices = list(range(len(atributosRestantes)))
            
            
                
            dic = diccionarioAtributosValores[atributosRestantes[contadorPosicion]]
            #print("diccionario: " + str(dic))
            #print("elem: " + str(elem))
            dic[elem][0] += 1
            if clase == claseMaxima:
                dic[elem][1] += 1
            contadorPosicion += 1
        
    print(str(diccionarioAtributosValores))           
    return diccionarioAtributosValores

class Clasificador:
    def __init__(self,clasificacion,clases,atributos, arbol):
        self.clasificacion=clasificacion
        self.clases=clases
        self.atributos=atributos
        self.arbol=arbol
        
    def entrena(self,entrenamiento,validacion=None):
        pass
    
    def clasifica(self, ejemplo):
        pass
    
    def evalua(self,prueba):
        pass
    
    def imprime(self):
        pass