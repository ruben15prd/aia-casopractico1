import prestamos
        
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
    
    
def aprendeRegla(indicesEntrenamiento,atributos, indicesAtributos):
    regla = []
    
    for indiceAtr in indicesAtributos:
        
        for valorAtributo in atributos[indiceAtr][1]:
            print(valorAtributo)
            condicion = (atributos,valorAtributo)
            
        
        
indices = list(range(len(prestamos.entrenamiento)))
#print(str(indices))
aprendeRegla(indices,prestamos.atributos, [0,1,2,3,4,5])    


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