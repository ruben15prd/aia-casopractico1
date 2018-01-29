import re

def generaDiccionarios():
    '''En esta funcion se genera el corpus, es decir, toda la estructura de datos necesaria para posteriormente poder
    calular las probabilidades para la prediccion de palabras y letras tanto unigram como bigram'''
    
    # Devolver una lista con 2 diccionarios, en una tenemos el corpus generado para las letras y en otro para las palabras
    # Para guardar las palabras, si hay un punto que la precede, entonces generaremos una lista con ceros
    
    
    #Diccionario clave: numero - valores : letras
    
    #Estructura palabras: clave: nºocurrencias,numeros correspondientes a la clave - lista: [la palabra anterior, los numeros de esa palabra,  nº de veces que aparece]  
    #Clave : 385723 Valor: [4,casa,[42,la,9]]
    
    #El número de caracteres se calcularia a demanda mediante el .length
    # Cuando tengamos un bigram de palabras cuando estemos consultando la segunda palabra, la primera ya no son números
    # Cuando no obtengamos resultado haciendo un bigram, hay que usar el modelo anterior.
    
    #Estructura letras: clave: letra, nºveces que aparece, posicion en la que se encuentra,[la letra anterior,  nº de veces que aparece]  
    
    # Definimos el diccionario que nos permitira realizar el mapeo entre numeros y letras
    diccionarioLetrasNumeros = {}
    
    diccionarioLetrasNumeros['1'] = ['a','á','b','c']
    diccionarioLetrasNumeros['2'] = ['d','e','é','f']
    diccionarioLetrasNumeros['3'] = ['g','h','i','í']
    diccionarioLetrasNumeros['4'] = ['j','k','l']
    diccionarioLetrasNumeros['5'] = ['m','n','ñ','o','ó']
    diccionarioLetrasNumeros['6'] = ['p','q','r','s']
    diccionarioLetrasNumeros['7'] = ['t','u','ú','v']
    diccionarioLetrasNumeros['8'] = ['w','x','y','z']
    
    # Definimos el diccionario para el corpus de letras
    
    corpusLetras = {}
    corpusPalabras = {}
    

    
    textoLista = []
    texto = ''
    
    for line in open("psicologia_revolucionaria.txt", 'r'):
        texto = texto + line
    
    #Eliminamos los caracteres especiales y no utiles y lo formateamos
    texto = texto.lower()
    textoSinCaracteresEspeciales = re.sub('[^a-zA-Z0-9-_*. áéíóúÁÉÍÓÚüÜñÑ]', '', texto)
    textoSinCaracteresEspeciales = re.sub('[ +]', '-', textoSinCaracteresEspeciales)
    textoSinCaracteresEspeciales = re.sub('-{2,}', '', textoSinCaracteresEspeciales)
    textoSinCaracteresEspeciales = re.sub('-', ' ', textoSinCaracteresEspeciales)
    #print(textoSinCaracteresEspeciales)
    
    
    #Dividimos el texto por los puntos
    textoLista = textoSinCaracteresEspeciales.split(".");
    
    corpusPalabras = generaDiccionarioPalabras(corpusPalabras, diccionarioLetrasNumeros, textoLista)
    
    
   
    
def generaDiccionarioPalabras(corpusPalabras,diccionarioLetrasNumeros, textoLista):
    palabraAnterior = ''
    
    for frase in textoLista:
        
        
        palabras = frase.split(" ")
        palabras = eliminaElementosLongitudMenor1(palabras)
        
        count = 0
        while (count < len(palabras)):
            palabra = palabras[count]
            
            #Cogemos la palabra anterior
            palabraAnterior = ''
            
            if count > 0:
                palabraAnterior = palabras[count - 1]
            else:
                palabraAnterior = ''
            
            #Insertamos las palabras en el diccionario
            corpusPalabras = insertaPalabra(corpusPalabras, diccionarioLetrasNumeros, palabra, palabraAnterior)
            
                
            
            count = count + 1
    
    
    print(corpusPalabras)
    return corpusPalabras
    



            
def eliminaElementosLongitudMenor1(lista):
    listaMayor1 = []
    for elem in lista:
        if len(elem) >= 1:
            listaMayor1.append(elem)
        
    return listaMayor1   
    
def insertaPalabra(corpusPalabras,diccionarioLetrasNumeros, palabra, palabraAnterior):
    
    palabraCodificada = codificar(palabra,diccionarioLetrasNumeros)
    palabraAnteriorCodificada = codificar(palabraAnterior,diccionarioLetrasNumeros)
    
    #En caso de que la palabra ya esta insertada
    if palabraCodificada in corpusPalabras:
        entradaCorpus = corpusPalabras[palabraCodificada]
        
        claveNumOcurrencias = entradaCorpus.get_claveNumOcurrencias().get_numOcurrenciasClave()
        
        claveNumOcurrenciasIncrementado = ClaveNumOcurrencias(entradaCorpus.get_claveNumOcurrencias().get_claveSinCodificar(),claveNumOcurrencias + 1)
        entradaCorpus.set_claveNumOcurrencias(claveNumOcurrenciasIncrementado)
        
    #Palabra no esta insertada 
    else:
        claveNumOc = ClaveNumOcurrencias(palabra,1)
        eg = EstructuraGuardado(claveNumOc,{})
        corpusPalabras[palabraCodificada] = eg
        
    # Contemplamos el caso de que tuviera palabra anterior
    if palabraAnterior != '':
        entradaCorpus = corpusPalabras[palabraCodificada]
        palabrasAnteriores = entradaCorpus.get_diccionarioPalabrasAnteriores()
        
        #En caso de que la palabra anterior ya esta insertada
        
        if palabraAnteriorCodificada in palabrasAnteriores:
            claveNumOcurrencias = palabrasAnteriores[palabraAnteriorCodificada]
            claveNumOcurrencias.set_numOcurrenciasClave(claveNumOcurrencias.get_numOcurrenciasClave() + 1)      
        # Palabra anterior no insertada 
        else:
            palabrasAnteriores[palabraAnteriorCodificada] = ClaveNumOcurrencias(palabraAnterior,1)
            
        
    return corpusPalabras
 
    
def codificar(palabra,diccionarioCodificacion):
    cadenaCodificada = ''
    for letra in palabra:
        for elem in diccionarioCodificacion:
            if letra in diccionarioCodificacion[elem]:
               cadenaCodificada = cadenaCodificada + elem 
               
    return cadenaCodificada

       
    
    

class EstructuraGuardado:
    def __init__(self, claveNumOcurrencias, diccionarioPalabrasAnteriores):
        self.claveNumOcurrencias = claveNumOcurrencias
        self.diccionarioPalabrasAnteriores = diccionarioPalabrasAnteriores
        
    def get_claveNumOcurrencias(self):
        return self.claveNumOcurrencias
    
    def get_diccionarioPalabrasAnteriores(self):
        return self.diccionarioPalabrasAnteriores
    
    def set_claveNumOcurrencias(self, claveNumOcurrencias):
        self.claveNumOcurrencias = claveNumOcurrencias
    
    def set_diccionarioPalabrasAnteriores(self, diccionarioPalabrasAnteriores):
        self.diccionarioPalabrasAnteriores = diccionarioPalabrasAnteriores
        
    def __str__(self):
        return str(self.claveNumOcurrencias) + "-" + str(self.diccionarioPalabrasAnteriores)

    def __repr__(self):
        return str(self.claveNumOcurrencias) + "-" + str(self.diccionarioPalabrasAnteriores)
    
class ClaveNumOcurrencias:
    def __init__(self, claveSinCodificar, numOcurrenciasClave ):
        self.claveSinCodificar = claveSinCodificar
        self.numOcurrenciasClave = numOcurrenciasClave
        
    def get_claveSinCodificar(self):
        return self.claveSinCodificar
    
    def get_numOcurrenciasClave(self):
        return self.numOcurrenciasClave
    
    def set_claveSinCodificar(self, claveSinCodificar):
        self.claveSinCodificar = claveSinCodificar
    
    def set_numOcurrenciasClave(self, numOcurrenciasClave):
        self.numOcurrenciasClave = numOcurrenciasClave
        
    def __str__(self):
        return str(self.claveSinCodificar) + "-" + str(self.numOcurrenciasClave)

    def __repr__(self):
        return str(self.claveSinCodificar) + "-" + str(self.numOcurrenciasClave)
