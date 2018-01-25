import re

def generaCorpus():
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
    
    '''
    for line in open("psicologia_revolucionaria.txt", 'r'):
        sp=line.split(".")
        for  word in sp:
            sp1 = word.split(" ")
            print(sp1, end='')
    '''
    
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
    
    palabraAnterior = ''
    
    for frase in textoLista:
        palabras = frase.split(" ")
        palabras = eliminaElementosLongitudMenor1(palabras)
        #print(palabras)
        count = 0
        while (count < len(palabras)):
            palabra = palabras[count]
            
            if count == 0:
                palabra = palabras[0]
                #numerosClave = codificar(palabra,diccionarioLetrasNumeros)
                #insertaPalabra(corpusPalabras, numerosClave)
                
            else:
                palabra = palabras[count]
            
            
            count = count + 1
    
    hola = ValorPalabra(3,"cosa","34", "si",3)
    corpusPalabras = insertaPalabra(corpusPalabras,'5742',hola)
    print(corpusPalabras)
                
   
    




            
def eliminaElementosLongitudMenor1(lista):
    listaMayor1 = []
    for elem in lista:
        if len(elem) >= 1:
            listaMayor1.append(elem)
        
    return listaMayor1   
    
def insertaPalabra(corpusPalabras, clave, palabraAnterior):
    corpusPalabras[clave] = palabraAnterior
    return corpusPalabras
 
    
def codificar(palabra,diccionarioCodificacion):
    cadenaCodificada = ''
    for letra in palabra:
        for elem in diccionarioCodificacion:
            if letra in diccionarioCodificacion[elem]:
               cadenaCodificada = cadenaCodificada + elem 
               
    return cadenaCodificada
    

class ValorPalabra:
    def __init__(self, numOcurrenciasClave, claveSinCodificar, palabraAnteriorCodificada, palabraAnteriorSinCodificar, numOcurrenciasPalabraAnterior):
        self.numOcurrenciasClave = numOcurrenciasClave
        self.claveSinCodificar = claveSinCodificar
        self.palabraAnteriorCodificada = palabraAnteriorCodificada
        self.palabraAnteriorSinCodificar = palabraAnteriorSinCodificar
        self.numOcurrenciasPalabraAnterior = numOcurrenciasPalabraAnterior
        
    def __str__(self):
        return str(self.numOcurrenciasClave) + "-" + str(self.claveSinCodificar) + "-" + str(self.palabraAnteriorCodificada) + "-" + str(self.palabraAnteriorSinCodificar) + "-" + str(self.numOcurrenciasPalabraAnterior)

    def __repr__(self):
        return str(self.numOcurrenciasClave) + "-" + str(self.claveSinCodificar) + "-" + str(self.palabraAnteriorCodificada) + "-" + str(self.palabraAnteriorSinCodificar) + "-" + str(self.numOcurrenciasPalabraAnterior)
