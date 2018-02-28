# -*- coding: utf-8 -*-
import votos
import random
import copy

class clasificador:
    def __init__(self,clases,norm=False): # norm = valor_columna_ejemplo-media_columna/desv. tipica
        self.clases = clases
        self.norm = norm
    
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,pesos_iniciales=None,rate_decay=False):
        
        pesosW = []
        if pesos_iniciales == None:
            pesosW = generaListaPesosAleatoriosW(len(entr[0]) +1)
        else:
            pesosW = pesos_iniciales
            
        pesosW = entrenaAux(entr,clas_entr,n_epochs,rate,self.clases)
        
        
        return pesosW
    
    # Devuelve la probabilidad de pertenecer a la clase 1. No se usa en el perceptrón.
    def clasifica_prob(self,ej):
        pass
    
    def clasifica(self,ej):
        pass
    

def entrenaAux(entr,clas_entr,n_epochs,rate,clases):
    """Funcion de entrenamiento"""
    pesosW = generaListaPesosAleatoriosW(len(entr[0]) +1)
        
          
    while n_epochs > 0:
        contadorEjemplo = 0
        for ejemplo in entr:
            ejemploAdd = generaListaElementoX(ejemplo)
                
            pesosW = actualizaPesosEjemplo(pesosW,ejemploAdd,rate,clases,clas_entr,contadorEjemplo)
                
            contadorEjemplo += 1
        n_epochs -= 1
        
    return pesosW

    
def umbral(x):
    """Funcion umbral"""
    resultado = 0
    if x >= 0:
        resultado = 1
    else:
        resultado = 0
        
    return resultado
        

def generaListaPesosAleatoriosW(longitud):
    """Genera la lista W de pesos aleatorios"""
    longitudAGenerar = longitud
    W = []
    
    while longitudAGenerar > 0:
        aleatorio = random.random()
        
        W.append(aleatorio)
        longitudAGenerar -= 1
    return W

def generaListaElementoX(ejemplo):
    """Dado un ejemplo le concatena el X0"""
    X0 = 1
    ejemplo = [X0] + ejemplo
    
    return ejemplo


def actualizaPesosEjemplo(listaPesosW,ejemplo,rate,clases,listaEjemplosClase,indiceEjemplo):
    """Actualiza la lista de pesos W, dado un ejemplo(recordar que este ejemplo tiene que incorporar X0)"""
    '''wi = wi + ηxi(y − o)'''
    pesosActualizados=[]
    
    
    diccionarioClases = generaMapeoClases(clases)
    
    
    longitudEjemplo = len(ejemplo)
    
    contador = 0
    while contador < longitudEjemplo:
        Xi = ejemplo[contador]
        Wi = listaPesosW[contador]
            
        clasificacionEjemplo = listaEjemplosClase[contador]
        y = diccionarioClases[clasificacionEjemplo]
        WixXi = Xi * Wi
        o = umbral(WixXi)
        
        WiFinal = Wi + rate*Xi*(y - o)
        pesosActualizados.append(WiFinal)
            
        contador += 1
        
    return pesosActualizados

def generaMapeoClases(clases):
    """Obtiene un diccionario con el mapeo de clases a digito"""
    diccionarioMapeoClases = {}
    
    contador = 0
    for clase in clases:
        diccionarioMapeoClases[clase] = contador
        contador += 1 

    return diccionarioMapeoClases


clasificador1 = clasificador(votos.votos_clases)
res = clasificador1.entrena(votos.votos_entr,votos.votos_entr_clas,100)
print(str(res))

'''
ejemplo = [-1,1,-1,1,1,1,-1,-1,-1,1,0,1,1,1,-1,1]
print("ejemplo a pelo: "  + str(ejemplo))
ejemploAdd = generaListaElementoX(ejemplo)
print("ejemplo add: "  + str(ejemploAdd))
print("len ejemplo add: "  + str(len(ejemploAdd)))

listaPesosAleatoria = generaListaPesosAleatoriosW(len(ejemploAdd))
print("listaPesosAleatoria: "  + str(listaPesosAleatoria))
print("len lista pesos aleatoria: "  + str(len(listaPesosAleatoria)))


res = actualizaPesosEjemplo(listaPesosAleatoria,ejemploAdd,0.1,votos.votos_clases,votos.votos_entr_clas,1)
print("resutlado : " + str(res))
'''