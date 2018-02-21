import prestamos_new
import numpy as np
import math

def calculaNumeroElementos(distribucion):
    numero = 0
    for elem in distribucion.values():
        numero += elem
    return numero

def aprendizajeArbolesDecision(conjuntoInicio, atributos, funcionClasificacion, cotaMinima=0, cotaMayoria=1):
    #conjuntoActual y atributosRestantes son listas de indices
    conjuntoActual = list(range(len(conjuntoInicio)))
    atributosRestantes = list(range(len(atributos)))
    
    
    nodo = aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes)
    
    
           
    return nodo
    #print(str(numero))
    
    
def aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes):

    # Crear parametro para almacenar la clase del nodo anterior y pasarsela al nodo hoja cuando no hay mas elementos, compruebaCasoBase=0
    # Si es caso base se construye un nodo hoja
    #print("----------------")
    #print("conjuntoActual: " + str(conjuntoActual))
    #print("atributosRestantes: " + str(atributosRestantes))
    
    instanciasClaseMaxima = calculaDistribucion(conjuntoInicio, conjuntoActual)
    claseMaxima = max(instanciasClaseMaxima, key=instanciasClaseMaxima.get)
    if compruebaCasoBase(conjuntoInicio, conjuntoActual, atributosRestantes, cotaMinima, cotaMayoria ) == 1:
        
        if len(conjuntoActual) == 1:#Nodo hoja
            nodo1 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                              atributo=None,
                              ramas=None,
                              clase=conjuntoInicio[conjuntoActual[0]][len(conjuntoInicio[conjuntoActual[0]])-1])
            
            distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
            atributo=None
            ramas=None
            clase=conjuntoInicio[conjuntoActual[0]][len(conjuntoInicio[conjuntoActual[0]])-1]
            
            '''
            print ("nodo1:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                       " -clase:" + str(clase))
            '''
            return nodo1
        else:#Nodo hoja
            nodo2 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                                   atributo=None,
                                   ramas=None,
                                   clase=claseMaxima)
            
            distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
            atributo=None
            ramas=None
            clase=claseMaxima
            
            '''
            print ("nodo2:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                       " -clase:" + str(clase))
            '''
            return nodo2
            
    else:
        
        dicRamas = {}
        
        # Si no es caso base se elige el mejor atributo atr(mejor atributo) usando la funcion clasifica(funcionClasificacion), dentro se ponen los distintos sumatorios de Entropia y los otros
        
        indiceMejorAtributo = obtenMejorAtributo(conjuntoInicio, atributos, conjuntoActual, atributosRestantes, funcionClasificacion)
        #print("indice: " + str(indiceMejorAtributo))
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
            #print(str(len(nuevoConjuntoActual)))
            if len(nuevoConjuntoActual) > 0:
                dicRamas[valor] = aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, nuevoConjuntoActual, atribRestantes)
            #print("atributosDespues:" + str(atributosRestantes) )
            #print("atributosRestantesDespues:" + str(atribRestantes) )
        
            # Se construye un nodo internmedio con distr, atr, ramas{valorAtributo: aprendizajeRecursivo(
            #       conjuntoInicio, atributos, porcentajeMinimo, porcentajeMayoria, nuevoConjuntoActual,
            #       atributosRestantes-atr)}
        
            # No hacer llamadas recursivas sin ejemplos
            if len(nuevoConjuntoActual) == 0:#Nodo hoja
                claseMaxima = max(instanciasClaseMaxima, key=instanciasClaseMaxima.get)
                nodo3 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                                   atributo=None,
                                   ramas=None,
                                   clase=claseMaxima)
                
                distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
                atributo=None
                ramas=None
                clase=claseMaxima
                
                '''
                print ("nodo3:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                       " -clase:" + str(clase))
                '''
                dicRamas[valor] = nodo3
                #return nodo3
                
        #print(str(len(dicRamas)))
        if len(dicRamas) > 0:#Nodo interno
            nodo4 = NodoDT(distr=calculaDistribucion(conjuntoInicio,conjuntoActual),
                                   atributo=indiceMejorAtributo,
                                   ramas=dicRamas,
                                   clase=None)
            
            distr=calculaDistribucion(conjuntoInicio,conjuntoActual)
            atributo=indiceMejorAtributo
            ramas=dicRamas
            clase=None
            
            
            '''
            print ("nodo4:" + "distribucion: " + str(distr) + " -atributo: " + str(atributo ) + " -ramas: " + str(ramas) + 
                       " -clase:" + str(clase))
            '''
            
            
            return nodo4
            
            
        
        
   
    
    
    #Guardamos el nodo raiz, que es lo que hay que guardar, no el arbol completo
    #1. Crear un nodo raiz conteniendo el conjunto inicial de entrenamiento D
    #2. REPETIR (hasta que no haya mas candidatos a nodos internos)
        #2.1 SELECCIONAR un nodo candidato a nodo interno
        #2.2 ELEGIR un criterio de decision
        #2.3 Crear los descendientes con los datos del nodo candidato que satisfacen el correspondiente valor del criterio de decision
    #3. ETIQUETAR cada nodo hoja con la clase dominante en los datos de dicho nodo (si no tiene datos, se usa la clase dominante en los datos del nodo padre)
    #4. PODAR nodos para evitar sobreajuste

def compruebaCasoBase(conjuntoInicio, conjuntoActual, atributosRestantes, cotaMinima=0, cotaMayoria=1):
    casoBase = 0
    if len(conjuntoActual) > 0:
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
    
    if len(conjuntoActual) > 0:  
        elemsMax = max(dicClase.values()) / len(conjuntoActual)
        if elemsMax > cotaMayoria:
            casoBase = 1
    #print (elemsMax)
        
    
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
        indiceAtributoMejor = 0
        valorErrorMinimo = 1.0
        for elem in atributosRestantes:
            error = 0.00
            #print(str(elem)) 
            #print(str(dic[elem]))
            for elem1 in dic[elem]:
                #print(str(elem1))
                    
                if dic[elem][elem1][0] > 0:
                    pd = dic[elem][elem1][1]
                    si = dic[elem][elem1][0]
                        
                    error += (si/tam)*(1 - (pd/si))
                      
            #print("atributo nuevo:"+str(error))
            
                
            impurezaTotalAtributo = impurezaPadre - error
            if impurezaTotalAtributo < valorErrorMinimo:
                valorErrorMinimo = error
                indiceAtributoMejor = elem
            
        #print(indiceAtributoMejor)
        return indiceAtributoMejor
                
    # Mide lo organizados que están los datos dentro del conjunto
    elif funcionClasificacion == "gini":
        distribucionClases = calculaDistribucion(conjuntoInicio,conjuntoActual)
        tam = len(conjuntoActual)
        #print ("distribucion:"+str(distribucionClases))
        pj = 0
       
        for clase in distribucionClases:
            pj += distribucionClases[clase]**2
            #print ("clase: " + str(distribucionClases[clase]))
       
        impurezaPadre = 1 - (pj/tam**2)
        #print ("impurezaPadre: " + str(impurezaPadre))
        #print("dic: "+str(dic))
       
        indiceAtributoMasOrganizado = 0
        valorOrganizacionMinimo = 1.0
        for elem in atributosRestantes:
            organizacion = 0.00
           
            for elem1 in dic[elem]:
                if dic[elem][elem1][0] > 0:
                    pi = dic[elem][elem1][0]**2
                    si = dic[elem][elem1][0]
                   
                    organizacion += (si/tam)*(1-pi)
           
            #print("atributo nuevo:" + str(organizacion))
                   
            impurezaTotalAtributo = impurezaPadre - organizacion  
            if impurezaTotalAtributo < valorOrganizacionMinimo:
                valorOrganizacionMinimo = organizacion
                indiceAtributoMasOrganizado = elem
       
        #print("indiceAtributoMasOrganizado: " + str(indiceAtributoMasOrganizado))
        return indiceAtributoMasOrganizado
    
    elif funcionClasificacion == "entropia":
        
        # Padre {'conceder': 6, 'no conceder': 2, 'estudiar': 7} --> - 6/15*log2(6/15) - 2/15*log2(2/15) - 7/15*log2(7/15)
        
        
        
        
        distribucionClases = calculaDistribucion(conjuntoInicio,conjuntoActual)
        #print ("distribucion:"+str(distribucionClases))
        tam = len(conjuntoActual)
        
        impurezaPadre = 0
       
        for clase in distribucionClases:
            valorClase = distribucionClases[clase]
            impurezaPadre -= ((valorClase/len(conjuntoActual))*math.log(valorClase,2))/(tam)
            #print ("clase: " + str(distribucionClases[clase]))
       
        #print ("impurezaPadre: " + str(impurezaPadre))
        #print("dic: "+str(dic))
       
        indiceAtributoMejor = 0
        valorErrorMinimo = 1.0
        for elem in atributosRestantes:
            error = 0.00
           
            for elem1 in dic[elem]:
                if dic[elem][elem1][0] > 0:
                    si = dic[elem][elem1][0]
                   
                    error -= (si*math.log(si,2))/tam
           
           # print("atributo nuevo:" + str(error))
                   
            impurezaTotalAtributo = impurezaPadre - error  
            if impurezaTotalAtributo < valorErrorMinimo:
                valorErrorMinimo = error
                indiceAtributoMejor = elem
       
        #print("indiceAtributoMejor: " + str(indiceAtributoMejor))
        return indiceAtributoMejor
        
    
    


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
        
    #print(str(diccionarioAtributosValores))           
    return diccionarioAtributosValores

class Clasificador:
    def __init__(self,clasificacion,clases,atributos):
        self.clasificacion=clasificacion
        self.clases=clases
        self.atributos=atributos
        self.nodoRaiz=None
        
    def entrena(self,entrenamiento,validacion=None):
        self.nodoRaiz = aprendizajeArbolesDecision(entrenamiento,atributos,"error", 0,1)
    
    def clasifica(self, ejemplo):
        
        indiceAtributo = self.nodoRaiz.atributo
            
        res = obtenSubnodo(self.nodoRaiz,ejemplo[indiceAtributo],ejemplo)
        print("Para el ejemplo: " + str(ejemplo) + " el valor de clasificacion es:")
        
        print(str(res))
        return res
        
    def evalua(self,prueba):
        aciertos = 0
        numTotal = len(prueba)
        
        for p in prueba:
            clasificacionArbol = self.clasifica(p)
            if clasificacionArbol == p[len(p) - 1]:
                aciertos = aciertos + 1
        
        rendimiento = aciertos/numTotal
        print(rendimiento)
        return rendimiento
                
    
    def imprime(self):
        
        arbol = imprimeRec(self.nodoRaiz,0)
        print(str(arbol))
    
def imprimeRec(nodo,contador):
    arbol = ''
    ramas = nodo.ramas
    arbol = arbol + "nodo" + str(contador) + ":" + "\n"
    contadorCopia = contador + 1
    
    if ramas != None:
        #print(atributos[nodo.atributo][0])
        arbol = arbol + "           atributo: " + atributos[nodo.atributo][0] +"\n"
        arbol = arbol + "           distribucion: " + imprimeDistribucion(nodo.distr) +"\n"
        subArbol = ''
        for rama in ramas:
            #print(type(ramas[rama]))
            
            nodoSub = ramas[rama]
            arbol = arbol + subArbol +  "           rama: "+ str(rama) + ",nodo" +str(contadorCopia) + "\n"
            #print(str(rama))
            arbol = arbol + subArbol + imprimeRec (nodoSub,contadorCopia)
            
            
    else:
        #print(str(nodo.clase))
        arbol = arbol + "           clase: "+  str(nodo.clase) + "\n"
    #print("-----------")
    
    return arbol


def imprimeDistribucion(distr):
    cadena = "{"
    for d in distr:
        #print(distr[d])
        cadena = cadena + str(d) + ":" + str(distr[d])+","
    cadena = cadena + "}"
    cadena = cadena.replace(",}", "}")
    return cadena

def obtenSubnodo(nodo,rama,ejemplo):
    ramas = nodo.ramas
    clase = ''
    
    indiceAtributo = nodo.atributo
    valorAtributo = ejemplo[indiceAtributo]
    if nodo.ramas != None:
            nuevoNodo = ramas[valorAtributo]
            
            indiceNuevoAtributo = nuevoNodo.atributo
            if indiceNuevoAtributo != None:
                
                valorNuevoAtributo = ejemplo[indiceNuevoAtributo]
                #print(str(indiceNuevoAtributo))
                clase = obtenSubnodo(nuevoNodo,valorNuevoAtributo,ejemplo)
                
            else:
                #print(clase)
                clase = clase +  nuevoNodo.clase
                
        
    else:
        #print(clase)
        clase = clase +  nodo.clase
    #print(clase)
    return clase
    
    

        
                  
clasificador1 = Clasificador("",clases,atributos)
clasificador1.entrena(entrenamiento)
clasificador1.imprime()
clasificador1.clasifica(['jubilado','ninguno','ninguna','uno','soltero','altos'])
clasificador1.evalua(prueba)