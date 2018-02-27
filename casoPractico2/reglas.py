import prestamos
import titanic
import votos
import math
import copy
import collections
import sys



class Clasificador:
    def __init__(self,clasificacion,clases,atributos):
        self.clasificacion=clasificacion
        self.clases=clases
        self.atributos=atributos
        self.reglas = None
        self.diccionarioDistribucionClases = None
        
    def entrena(self,entrenamiento,validacion=None,prepoda = 1):
        self.reglas = aprendeReglasEntrenamiento(entrenamiento,self.atributos,list(range(len(self.atributos))),self.clases,prepoda)  
        self.diccionarioDistribucionClases = diccionarioNumeroElementosClase(entrenamiento,self.clases)
        
        
        print("Reglas antes de la poda:")
        print( str(self.reglas))
        if validacion != None:
            print("Reglas despues de la pospoda:")
            self.reglas = pospoda(self.reglas,validacion,self.diccionarioDistribucionClases)
        
        
    def clasifica(self,ejemplo):
        res = clasificaElemento(self.reglas,ejemplo,self.diccionarioDistribucionClases)
        return res
        
    def evalua(self,prueba):
        rendimiento = evaluaAux(self.diccionarioDistribucionClases,self.reglas,prueba)
        return rendimiento 
        
    def imprime(self):
        diccionarioDistribucionClasesCopia = copy.deepcopy(self.diccionarioDistribucionClases)
        contador = 0
        while len(diccionarioDistribucionClasesCopia) > 0:
            claveMinima = obtenClaveMinimaPorValor(diccionarioDistribucionClasesCopia)
            diccionarioDistribucionClasesCopia.pop(claveMinima, None)
            print("Reglas aprendidas para la clase: " +  claveMinima + "\n")
            
            reglasClave = self.reglas[contador]
            for regla in reglasClave:
                print(str(regla))
            print("\n\n")
            contador += 1 



#Una regla es una lista de tuplas ([(indiceAtributo,valor)] ,clasificacion)
def reglaCubreElemento(regla, elemento):
    '''Metodo que comprueba si una regla cubre a un elemento'''
    cubre = 1
    
    if len(regla[0]) == 0:
        cubre = 0
        
    else:
    
        for condicion in regla[0]:
        
            indiceAtributo = condicion[0]
            valorAtributo = condicion[1]
        
            if valorAtributo != elemento[indiceAtributo]:
                cubre = 0
            
    return cubre



def reglaCubreCorrectamenteElemento(regla, elemento):
    '''Metodo que comprueba si una regla cubre correctamente a un elemento'''
    cubre = 1
    
    if len(regla[0]) == 0:
        cubre = 0
    else:
        for condicion in regla[0]:
            
            indiceAtributo = condicion[0]
            valorAtributo = condicion[1]
            valorClasificacion = regla[1]
            #print("----")
            #print(str(indiceAtributo))
            #print(str(valorAtributo))
            #print(str(valorClasificacion))
            if valorAtributo != elemento[indiceAtributo] or valorClasificacion != elemento[len(elemento) - 1] :
                cubre = 0
    
    return cubre



# Eliminamos los elementos cubiertos por la regla
def numeroElementosCubiertos(regla, elementos): 
    '''Metodo que devuelve el numero de elementos cubiertos'''
    numeroCubiertos = 0
    
    for e in elementos:
        if reglaCubreElemento(regla,e) == 1:
            numeroCubiertos += 1
            
    return numeroCubiertos

def numeroElementosCubiertosCorrectamente(regla, elementos):
    '''Metodo que devuelve el numero de elementos cubiertos correctamente'''
    numeroCubiertosCorrectamente = 0
    
    for e in elementos:
        if reglaCubreCorrectamenteElemento(regla,e) == 1:
            numeroCubiertosCorrectamente += 1
            
    return numeroCubiertosCorrectamente


                
def frecuenciaRelativa(regla,entrenamiento):
    '''Metodo que calcula la frecuencia relativa de una regla en el conjunto de entrenamiento'''
    
    '''
    FR(S,R) = p/t p= numero de ejemplos cubiertos por R de S, t = numero de ejemplos cubiertos correctamente por R de S
    ''' 
    t = numeroElementosCubiertos(regla,entrenamiento)
    p = numeroElementosCubiertosCorrectamente(regla,entrenamiento)
    
    #print("numerosCubiertosCorrectamente: " + str(p))
    #print("numerosCubiertos: " + str(t))
    
    if t != 0:
        frecuenciaRelativa = p/t
    else:
        frecuenciaRelativa = 0
    
    return frecuenciaRelativa



def gananciaInformacion(entrenamiento,regla,reglaAmpliada):
    '''
    La ganancia de informacion de una regla ampliada R+ con respecto a la original R es
    G(R; R+; S) = p*(log2(p+/t+) - log2(p/t))
    
    donde t (t+) es el numero de ejemplos de S cubiertos por R (R+)
    y p (p+) es el numero de ejemplos de S correctamente cubiertos
    por R (R+)
    '''
    p = numeroElementosCubiertosCorrectamente(regla,entrenamiento)
    pAmpliada = numeroElementosCubiertosCorrectamente(reglaAmpliada,entrenamiento)
    t = numeroElementosCubiertos(regla,entrenamiento)
    tAmpliada = numeroElementosCubiertos(reglaAmpliada,entrenamiento)
    
    ganancia = p*(math.log((pAmpliada/tAmpliada),2) - math.log((p/t),2))
    
    return ganancia



def aprendeConjuntoReglasClase(entrenamiento,atributos,indicesAtributos,clase, umbralPrepoda):
    '''Metodo que aprende un conjunto de reglas para una clase'''
    entrenamientoCopia = copy.deepcopy(entrenamiento)
    atributosCopia = copy.deepcopy(atributos)
    reglas = []
    
    longitudElementosClase = len(filtraEntrenamientoPorClase(entrenamientoCopia,clase))
    
    #while frecuenciaRelativaReglaTotal < umbralPrepoda and longitudElementosClase > 1:
    
    
    while longitudElementosClase > 0:
        #print("longitud:" + str(longitudElementosClase))
        
        #print("-----------------------------------")
        resultado = aprendeRegla(entrenamientoCopia,atributosCopia,indicesAtributos,clase, umbralPrepoda)
        #print(str(resultado[1]))
        entrenamientoCopia = copy.deepcopy(resultado[0])
        #atributosCopia = copy.deepcopy(resultado[1])
        #print(str(resultado[1][0]))
        if len(resultado[1][0]) > 0: 
            reglas.append(resultado[1])
        #print(str(resultado[1]))
        longitudElementosClase = len(filtraEntrenamientoPorClase(entrenamientoCopia,clase))
        #print("entro :" + str(longitudElementosClase))
        #print("entro :" + str(len(entrenamientoCopia)))
    #print(str(reglas))
    return reglas



def aprendeReglasEntrenamiento(entrenamiento,atributos,indicesAtributos,clases, umbralPrepoda):
    '''Metodo que aprende las reglas para el conjunto de entrenamiento'''
    diccionarioDistribucionClases = diccionarioNumeroElementosClase(entrenamiento,clases)
    reglasClases = []
    
    while len(diccionarioDistribucionClases) > 0:
        claveMinima = obtenClaveMinimaPorValor(diccionarioDistribucionClases)
        diccionarioDistribucionClases.pop(claveMinima, None)
        resultado = aprendeConjuntoReglasClase(entrenamiento,atributos,indicesAtributos,claveMinima, umbralPrepoda)
        reglasClases.append(resultado)
        #print(str(reglasClases))
    #print(str(reglasClases))
    return reglasClases



def obtenClaveMinimaPorValor(diccionarioDistribucionClases):
    '''Metodo que obtiene el valor de clasificacion de la clase que menos aparece'''
    min_value = 9223372036854775807
    for key in diccionarioDistribucionClases:
        if min_value is None or min_value > diccionarioDistribucionClases[key]:
            min_value = diccionarioDistribucionClases[key]
            min_key = key  
            
    return min_key



def diccionarioNumeroElementosClase(entrenamiento,clases):
    '''Metodo que devuelve el numero de elementos de cada clase'''
    frecuenciaClasificacionClases = {}
    print("")
    for clase in clases:
        frecuenciaClasificacionClases[clase] = 0
        #print(str(clase))
    for elem in entrenamiento:
        claseElemento = elem[len(elem) -1]
        frecuenciaClasificacionClases[claseElemento] += 1
    
    return frecuenciaClasificacionClases



def elementosPorCubrirRegla(regla,elementos):
    '''Metodo que devuelve el numero de elementos que faltan por cubrir dado una regla'''
    elementosPorCubrir = []
    
    for e in elementos:
        if reglaCubreElemento(regla,e) == 0:
            elementosPorCubrir.append(e)    
            
    return elementosPorCubrir
'''   
def eliminaTodasOcurrenciasLista(lista,elemento):
    Metodo que elimina todas la ocurrencias de un elemento en una lista
    copiaLista = []
    elemento  = elemento[0:len(elemento) - 1]
    for elem in lista:
        quitaClase = elem[0:len(elem) - 5]
        copiaLista.append(quitaClase)
    
    
    print("eiii:" + str(elemento))
    print("wooo2:" + str(lista))
    while elemento in copiaLista:
        copiaLista.remove(elemento)
    
    return lista
#indices = list(range(len(prestamos.entrenamiento)))
#print(str(indices))
'''



def filtraEntrenamientoPorClase(entrenamiento,clase):
    '''Metodo que devuelve los elementos que pertecen a una clase'''
    filtrado = []
    
    for e in entrenamiento:
        if e[len(e) - 1] == clase:
            filtrado.append(e)
            
    return filtrado



def aprendeRegla(entrenamiento,atributos,indicesAtributos,clase, umbralPrepoda):
    regla = ([],clase)
    #print("longitud entrenamiento: " + str(entrenamiento))
    #print("longitud entrenamiento: " + str(len(entrenamiento)))
    #print("atributos: " + str(atributos))
    entrenamientoCopia = copy.deepcopy(entrenamiento)
    atributosCopia = copy.deepcopy(atributos)
    indicesAtributosCopia = copy.deepcopy(indicesAtributos)
   
    #regla = ([(0,"jubilado")],"estudiar")
    
    #['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar']
    frecuenciaRelativaReglaTotal = 0
    
    
    '''Añadir la condicion que cuando se quede sin atributos devolver la regla'''
    while frecuenciaRelativaReglaTotal < umbralPrepoda and len(indicesAtributosCopia) > 0:
        #print("frecuencia Relativa :" + str(frecuenciaRelativaReglaTotal))
        frecuenciaRelativaReglaActual = 0
         # Esta variable nos almacena la regla que mejor frecuencia relativa tiene
        #en cada iteracion
        #Iteramos los atributos 
        regla_max = ([],clase)
        #print("indicesAtr: " + str(indicesAtributosCopia))
        for indiceAtributo in indicesAtributosCopia:
            #print("----------------------------------------")
            #print("regla : " + str(regla))
            atr = atributosCopia[indiceAtributo][1]
            #print(str(atr))
            # Iteramos los atributos restantes  
            for valorAtributo in atr:
                #print(str(valorAtributo))
                regla_aux = copy.deepcopy(regla)
                regla_aux[0].append((indiceAtributo,valorAtributo))
                #print("aux: "+str(regla_aux))
                frecuenciaRelativaReglaMax = frecuenciaRelativa(regla_aux,entrenamientoCopia)
                #print("freq: "+str(frecuenciaRelativaReglaMax))
                if frecuenciaRelativaReglaMax >= frecuenciaRelativaReglaActual:
                    #Copiamos el valor de la regla_aux a regla_max
                    regla_max = copy.deepcopy(regla_aux)
                    frecuenciaRelativaReglaActual = frecuenciaRelativaReglaMax
        #print("*******************")
        #Si la reglaMax era mejor que la regla actual se sustituye su valor por la regla con 
        #nuevas condiciones
        #print(str(regla_max))
        #print("aqui:" + str(frecuenciaRelativaReglaTotal))
        if frecuenciaRelativaReglaActual > frecuenciaRelativaReglaTotal:
            #Guardamos en nuestra regla actual la regla con maxima frecuencia
            
            regla = copy.deepcopy(regla_max)
            ultimaReglaAñadida = regla[0][-1]
            indiceUltimaReglaAñadida = ultimaReglaAñadida[0]
            valorUltimaReglaAñadida = ultimaReglaAñadida[1]
            atributosCopia[indiceUltimaReglaAñadida][1].remove(valorUltimaReglaAñadida)
            indicesAtributosCopia.remove(indiceUltimaReglaAñadida)
            frecRegla =  frecuenciaRelativa(regla,entrenamientoCopia)
            #print("tmp: " + str(frecRegla))
            #Actualizamos la frecuencia relativa total
            frecuenciaRelativaReglaTotal = frecRegla
            
            #print("regla ultima: " + str(ultimaReglaAñadida))    
            #print("atributosCopia: " + str(atributosCopia))
            
    #Nos quedamos con los elementos no cubiertos correctamente
    #print("len: " + str(len(regla[0])))
    if len(regla[0]) >= 1:
        entrenamientoCopia = elementosPorCubrirRegla(regla,entrenamientoCopia)
    '''
    print("regla: " + str(regla))
    
    print("")
    print("entrenamientoCopia: " + str(entrenamientoCopia))
    print("")
    print("longitud entrenamiento: " + str(len(entrenamiento)))
    print("")
    print("longitud entrenamientoCopia: " + str(len(entrenamientoCopia)))
    print("")
    print("regla: " + str(regla))
    print("----------------------")
    '''
    return (entrenamientoCopia,regla)



def pospoda(reglas,validacion,diccionarioDistribucionClases):
    '''Metodo de poda de reglas'''
    reglasCopia = copy.deepcopy(reglas)
    
    reglasFinales = podaReglasConjunto(reglasCopia, validacion, diccionarioDistribucionClases)
    
    return reglasFinales 



def podaReglasConjunto(reglas, validacion, diccionarioDistribucionClases):
    '''Metodo que poda una regla de un conjunto de reglas'''
    
    reglasFinales = copy.deepcopy(reglas)
    rendimientoFinal = evaluaPoda(diccionarioDistribucionClases, reglasFinales, validacion) # Evalua el rendimiento antes de la poda
    
    # Eliminar una condicion
    reglaModificada = None
    for conjuntoReglas in reglasFinales:
        
        for regla in conjuntoReglas:
            
            reglaModificada = copy.deepcopy(regla)
            longitud = len(reglaModificada[0]) # Longitud de las condiciones
            if longitud > 1:
                print("--------------------------")
                #print("regla antes: "+ str(reglaModificada))
                reglaModificada = eliminaCondicion(reglaModificada) 
                #print("regla despues: "+ str(reglaModificada))
                #print("CONJUNTO ANTES:\n"+ str(conjuntoReglas))
                nuevoConjuntoReglas = reemplazaRegla(reglasFinales,regla, reglaModificada)
                #print("CONJUNTO DESPUES:\n"+ str(nuevoConjuntoReglas))
                rendimiento = evaluaPoda(diccionarioDistribucionClases,nuevoConjuntoReglas,validacion)
                #print("rendimiento Antes: "+ str(rendimientoFinal))
                print("rendimiento despues: "+ str(rendimiento))
                if rendimiento > rendimientoFinal:
                    reglasFinales = nuevoConjuntoReglas
                    rendimientoFinal = rendimiento
                        
    '''                   
    #Eliminar una regla
    for conjuntoReglas in reglasFinales:
        
        for regla in conjuntoReglas:
            print("conjunto antes: "+ str(conjuntoReglas))
            nuevoConjuntoReglas = eliminaRegla(reglas,regla)
            print("conjunto despues: "+ str(nuevoConjuntoReglas))
            
            rendimiento = evaluaAux(diccionarioDistribucionClases,reglas,nuevoConjuntoReglas)
            print("rendimiento Antes: "+ str(rendimientoFinal))
            print("rendimiento despues: "+ str(rendimiento))
            if rendimiento > rendimientoFinal:
                reglasFinales = nuevoConjuntoReglas
                rendimientoFinal = rendimiento   
         
    '''
    
    return reglasFinales



def reemplazaRegla(reglas,reglaOriginal, reglaSustitucion):
    '''Metodo que devuelve el conjunto de reglas sustituyendo la reglaOriginal por la reglaSustitucion'''
    copiaReglas = copy.deepcopy(reglas)
    reglasFinal = []
    
    for conjuntoReglas in copiaReglas:
        for regla in conjuntoReglas:
        
            print("regla: " +str(regla))
            if compruebaReglasIguales(regla,reglaOriginal) == 1:
                print("entro en el if")
                reglasFinal.append(reglaSustitucion)
                
            else:
                print("entro en el else")
                reglasFinal.append(regla)
    
    return reglasFinal



def eliminaRegla(reglas,reglaAEliminar):
    copiaReglas = copy.deepcopy(reglas)
    copiaReglas.remove(reglaAEliminar)
               
    return copiaReglas


def reemplazaEliminaRegla(reglas,reglaOriginal, reglaSustitucion):
    '''Metodo que devuelve el conjunto de reglas sustituyendo la reglaOriginal por la reglaSustitucion'''
    copiaReglas = copy.deepcopy(reglas)
    #indice = reglas.index(reglaOriginal)
    
    if len(reglaSustitucion) > 0:
        #Si la regla tiene condiciones la sustituimos en el conjunto de reglas
        for i,v in enumerate(copiaReglas):
            #print("v:" + str(v) + "reglaoriginal: " + str(reglaOriginal))
            if compruebaReglasIguales(v,reglaOriginal) == 1:
                #print("reemplaza")
                copiaReglas.pop(i)
                copiaReglas.insert(i, reglaSustitucion)
    
    else:
        #Si la regla no tiene condiciones eliminamos la regla del conjunto
        for i,v in enumerate(copiaReglas):
            #print("v:" + str(v) + "reglaoriginal: " + str(reglaOriginal))
            if compruebaReglasIguales(v,reglaOriginal) == 1:
                #print("reemplaza")
                copiaReglas.pop(i)
    
    
    
    return copiaReglas



def compruebaReglasIguales(regla1,regla2):
    '''Comprueba si dos reglas son iguales'''
    contador = 0 
    
    igual = 1
    while contador <= 1:
        if regla1[contador] != regla2[contador]:
            igual = 0
        contador = contador + 1
    
    return igual
    
    

def eliminaCondicion(regla):
    '''Elimina una condicion de una regla'''
    reglaModificada = ([],regla[1])
    
    reglaCopia = copy.deepcopy(regla)
    
    
    condiciones = reglaCopia[0]
    condiciones.pop()
    
    for condicion in condiciones:
        reglaModificada[0].append(condicion)
    
    return reglaModificada



def clasificaElemento(reglas,ejemplo,diccionarioDistribucionClases):
    '''Metodo que clasifica un elemento dado'''
    diccionarioDistribucionClasesCopia = copy.deepcopy(diccionarioDistribucionClases)
    #print("reglas: " + str(reglas))
    
    res = 0
    contador = 0
    while len(diccionarioDistribucionClasesCopia) > 0:
        claveMinima = obtenClaveMinimaPorValor(diccionarioDistribucionClasesCopia)
        #print(claveMaxima)
        diccionarioDistribucionClasesCopia.pop(claveMinima, None)
            
        reglasClave = reglas[contador]
            
            
        for regla in reglasClave:
            clasifica = 1
            #print("clasifica: " + str(clasifica))
            #print("regla: " + str(regla))
            #print("regla de 0: " + str(regla[0]))
                
            for condicion in regla[0]:
                print("condicion: " + str(condicion))
                indice = condicion[0]
                valorRegla = condicion[1]
                #print("indice: " + str(condicion[0]) + "valor: " + str(condicion[1]))
                #print("ejmplo:"  + str(ejemplo[indice]))
                if ejemplo[indice] != valorRegla:
                    clasifica = 0
                    
            if clasifica == 1:
                #Se obtiene el valor de clasificacion
                res = 1
                return regla[1]
                    
            
        contador += 1 
        
    if res == 0:
        #Se asigna el valor de clasificacion dominante
        return reglas[len(reglas)-1][-1][1]



def evaluaAux(diccionarioDistribucionClases,reglas,prueba):
    '''Metodo para evaluar'''
    aciertos = 0
    numTotal = len(prueba)
    for p in prueba:
        clasificacionArbol = clasificaElemento(reglas,p,diccionarioDistribucionClases)
        if clasificacionArbol == p[len(p) - 1]:
            aciertos = aciertos + 1
        
    rendimiento = aciertos/numTotal
    print("El rendimiento es: " + str(rendimiento))
    return rendimiento



def evaluaPoda(diccionarioDistribucionClases,reglas,prueba):
    '''Metodo para evaluar desde el metodo de la pospoda'''
    aciertos = 0
    numTotal = len(prueba)
        
    for p in prueba:
        #print("p: " + str(p[0:len(p)- 1]))
        #print("reglas: " + str(reglas))
        print("elemento a evaluar: " + str(p[0:len(p)- 1]))
        clasificacionArbol = clasificaElemento(reglas,p[0:len(p)- 1],diccionarioDistribucionClases)
        if clasificacionArbol == p[len(p) - 1]:
            aciertos = aciertos + 1
        
    rendimiento = aciertos/numTotal
    print("El rendimiento es: " + str(rendimiento))
    return rendimiento


#res = clasificador1.clasifica(['laboral','dos o más','una','uno','soltero','bajos'])
#print("El valor de clasificacion para el ejemplo es: " + str(res))

#clasificador1.evalua(prestamos.prueba)



#Funciones:
#Aprende una regla para un conjunto de entrenamiento
#Aprende varias reglas para un conjunto de entrenamiento
#Aprende varias reglas para varios conjuntos de entrenamiento

# En primer caso hay que ver que los elementos que cubra la regla sean cubiertos correctamente
# En el segundo caso hay que ver que que cubra correctamente todos los elementos de la clase 
# En el tercer caso habria que llamar al segundo caso para cada una de las posibles clases

# Si agotamos los atributos estamos poniendo un ejemplo
# Para la poda se puede o bien eliminar una regla o eliminar una condicion de la regla, habra que ir calculando
# todas las posibles combinaciones y quedarnos con aquellos que clasifiquen mejor el conjunto de prueba
# Si hay un empate en el numero de elementos que recubren varias reglas nos quedamos con aquella que cubra mas ejemplos   
'''
g = numeroElementosCubiertos(([(0, 'parado'),(5, 'bajos')], 'conceder'),prestamos.entrenamiento1)
l = numeroElementosCubiertosCorrectamente(([(0, 'parado'),(5, 'bajos')], 'conceder'),prestamos.entrenamiento1)
print("g: " + str(g))
print("l: " + str(l))
woo = elementosPorCubrirRegla(([(0, 'parado'),(5, 'bajos')], 'conceder'),prestamos.entrenamiento1)
print("lol: " + str(woo))
print("len entrenamiento: " + str(len(woo)))
'''


#res =  aprendeRegla(prestamos.entrenamiento1,prestamos.atributos,[0,1,2,3,4,5],"conceder", 1)
#res2 = aprendeConjuntoReglasClase(prestamos.entrenamiento1,prestamos.atributos,[0,1,2,3,4,5],"conceder", 1)
#print("res: " + str(res))

#res = aprendeConjuntoReglasClase(prestamos.entrenamiento1,prestamos.atributos,[0,1,2,3,4,5],"conceder", 1)
#print("resultado: " + str(res))


#res = compruebaReglasIguales(([(0, 'parado'),(5, 'bajos')], 'conceder'),([(1, 'uno'),(5, 'bajos')], 'conceder'))

#res = eliminaCondicion(([(0, 'parado')], 'conceder'))  

#print(str(res))


#res = compruebaReglasIguales(([(0, 'parado'),(5, 'bajos')], 'conceder'),([(0, 'parado')], 'conceder'))
#print(str(res))

'''
#Titanic
print("-------------------")
#indicesAtributosTitanicSeleccionados =  [1,6,8]
#atributosSeleccionados = [titanic.atributos[i] for i in indicesAtributosTitanicSeleccionados]

clasificador1 = Clasificador("",titanic.clases,titanic.atributos)
clasificador1.entrena(titanic.entrenamiento[0:100],titanic.validacion,1)
clasificador1.imprime()
res = clasificador1.clasifica(["1","1st","Cardeza, Mrs James Warburton Martinez (Charlotte Wardle Drake)","adulto","Cherbourg","Germantown, Philadelphia, PA","B-51/3/5","17755 L512 6s","3","female"])
print("El valor de clasificacion para el ejemplo es: " + str(res))
clasificador1.evalua(titanic.prueba)
'''

'''
#Votos
print("-------------------")
clasificador2 = Clasificador("",votos.clases,votos.atributos)
clasificador2.entrena(votos.entrenamiento,1)
clasificador2.imprime()
res = clasificador2.clasifica(['n','s','n','s','s','s','n','n','n','s','?','s','s','s','n','s'])
print("El valor de clasificacion para el ejemplo es: " + str(res))
clasificador2.evalua(votos.prueba)
'''


#Prestamos
print("-------------------")
clasificador3 = Clasificador("",prestamos.clases,prestamos.atributos)
clasificador3.entrena(prestamos.entrenamiento,prestamos.validacion,1)
#clasificador3.imprime()
#res = clasificador3.clasifica(['jubilado','ninguno','ninguna','uno','soltero','altos'])
#print("El valor de clasificacion para el ejemplo es: " + str(res))
#clasificador3.evalua(prestamos.prueba)








 