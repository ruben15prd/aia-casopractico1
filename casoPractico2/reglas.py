import prestamos
import math
import copy
  
class Clasificador:
    def __init__(self,clasificacion,clases,atributos):
        self.clasificacion=clasificacion
        self.clases=clases
        self.atributos=atributos
        
    def entrena(self,entrenamiento,validacion=None):
        pass
        
        
        
        
    def clasifica(self,ejemplo):
        pass
    def evalua(self,prueba):
        pass
    def imprime(self):
        pass

#Una regla es una lista de tuplas ([(indiceAtributo,valor)] ,clasificacion)
def reglaCubreElemento(regla,elemento):
    
    cubre = 1
    
    for condicion in regla[0]:
        
        indiceAtributo = condicion[0]
        valorAtributo = condicion[1]
        
        if valorAtributo != elemento[indiceAtributo]:
            cubre = 0
    
    return cubre


def reglaCubreCorrectamenteElemento(regla, elemento):
    cubre = 1
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

def numeroElementosCubiertos(regla,elementos): 
    numeroCubiertos = 0
    
    for e in elementos:
        if reglaCubreElemento(regla,e) == 1:
            numeroCubiertos += 1
            
    return numeroCubiertos

def numeroElementosCubiertosCorrectamente(regla, elementos):
    numeroCubiertosCorrectamente = 0
    
    for e in elementos:
        if reglaCubreCorrectamenteElemento(regla,e) == 1:
            numeroCubiertosCorrectamente += 1
            
    return numeroCubiertosCorrectamente
    

    
            

def frecuenciaRelativa(regla,entrenamiento):
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
'''
def aprendeConjuntoReglasClase(entrenamiento,atributos,indicesAtributos,clase, umbralPrepoda):
    entrenamientoCopia = entrenamiento[:]
    atributosCopia = atributos[:]
    reglas = []
    while len(entrenamientoCopia) > 0:
        
        for e in entrenamientoCopia:
             resultado = aprendeReglaClase(entrenamientoCopia,atributosCopia,indicesAtributos,clase, umbralPrepoda)   
             entrenamientoCopia1 = resultado[0]
             atributosCopia1 = resultado[1]
             reglas.append(resultado[3])
'''    
    
    
    
    
    
    
def elementosPorCubrirRegla(regla,elementos):
    elementosPorCubrir = elementos[:]
    
    for e in elementosPorCubrir:
        if reglaCubreCorrectamenteElemento(regla,e) == 1:
                elementosPorCubrir = eliminaTodasOcurrenciasLista(elementosPorCubrir,e)
            
            
    return elementosPorCubrir
    
def eliminaTodasOcurrenciasLista(lista,elemento):
    
    while elemento in lista:
        lista.remove(elemento)
    return lista
#indices = list(range(len(prestamos.entrenamiento)))
#print(str(indices))
    
def filtraEntrenamientoPorClase(entrenamiento,clase):
    filtrado = []
    
    for e in entrenamiento:
        if e[len(e) - 1] == clase:
            filtrado.append(e)
            
    return filtrado



def aprendeReglaClase(entrenamiento,atributos,indicesAtributos,clase, umbralPrepoda):
    regla = ([],clase)
    
    entrenamientoCopia = entrenamiento[:]
    atributosCopia = atributos[:]
   
    #regla = ([(0,"jubilado")],"estudiar")
    
    #['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar']
    frecuenciaRelativaReglaTotal = 0
    
    while frecuenciaRelativaReglaTotal < umbralPrepoda:
        
        frecuenciaRelativaReglaActual = 0
        regla_max = ([],clase)
        #while frecuenciaRelativaRegla < umbralPrepoda:
            #print("----------------------------------------")
            
        for indiceAtributo in indicesAtributos:
            #print("----------------------------------------")
            #print("regla : " + str(regla))
            atr = atributosCopia[indiceAtributo][1]
            #print(str(atr))
                
            for valorAtributo in atr:
                #print(str(valorAtributo))
                regla_aux = copy.deepcopy(regla)
                regla_aux[0].append((indiceAtributo,valorAtributo))
                #print("aux: "+str(regla_aux))
                frecuenciaRelativaReglaMax = frecuenciaRelativa(regla_aux,entrenamientoCopia)
                #print("freq: "+str(frecuenciaRelativaReglaMax))
                if frecuenciaRelativaReglaMax > frecuenciaRelativaReglaActual:
                    regla_max = copy.deepcopy(regla_aux)
                    frecuenciaRelativaReglaActual = frecuenciaRelativaReglaMax
        #print("*******************")
        
        if frecuenciaRelativaReglaActual > frecuenciaRelativaReglaTotal:
            #Guardamos en nuestra regla actual la regla con maxima frecuencia
            regla = copy.deepcopy(regla_max)
            ultimaReglaAñadida = regla[0][-1]
            indiceUltimaReglaAñadida = ultimaReglaAñadida[0]
            valorUltimaReglaAñadida = ultimaReglaAñadida[1]
            atributosCopia[indiceUltimaReglaAñadida][1].remove(valorUltimaReglaAñadida)
            frecRegla =  frecuenciaRelativa(regla,entrenamientoCopia)
            #print("tmp: " + str(frecRegla))
            frecuenciaRelativaReglaTotal = frecRegla
                
            
            
            #print("regla ultima: " + str(ultimaReglaAñadida))    
            #print("atributosCopia: " + str(atributosCopia))
            
    #Nos quedamos con los elementos no cubiertos correctamente
    entrenamientoCopia = elementosPorCubrirRegla(regla,entrenamientoCopia)
    
    #print("atributosCopia: " + str(atributosCopia))
    #print("entrenamientoCopia: " + str(entrenamientoCopia))
    #print("longitud entrenamiento: " + str(len(entrenamiento)))
    #print("longitud entrenamientoCopia: " + str(len(entrenamientoCopia)))
    #print("regla: " + str(regla))
    
    return (entrenamientoCopia,atributosCopia,regla)

aprendeReglaClase(prestamos.entrenamiento,prestamos.atributos,[0,1,2,3,4,5],"conceder",1)    


'''
a = numeroElementosCubiertos((([0,"hola"],[1,"adios"]),"si"),[["hola", "adios", "si"],["hola", "adios", "no"]])
print(str(a))
'''



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