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
    
    diccionarioLetras = {}
    diccionarioPalabras = {}
    

    
    textoLista = []
    texto = ''
    
    for line in open("prueba.txt", 'r'):
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
    
    
    diccionarioPalabras = generaDiccionarioPalabras(diccionarioPalabras, diccionarioLetrasNumeros, textoLista)
    diccionarioLetras = generaDiccionarioLetras(diccionarioLetras, diccionarioLetrasNumeros, textoLista)
    print("Palabras: ")
    print(diccionarioPalabras)
    print("Letras: ")
    print(diccionarioLetras)
    
    #numLetra = input ("Escriba un número: ")
    #letraAnterior = input ("Escriba una letra anterior: ")
    
    
    #numPalabra = input ("Escriba varios número: ")
    #palabraAnterior = input ("Escriba una palabra anterior: ")
    
    #uniL = uniLetras(numLetra, diccionarioLetras)
    #biL = biLetras(letraAnterior, numLetra, diccionarioLetras)
    #uniP = uniPalabras(numPalabra, diccionarioPalabras)
    #biP = biPalabras('hola', '1111', diccionarioPalabras)
    #print(uniL)
    #print(biL)
    #print(uniP)
    #print(biP)
    
    
    return (diccionarioLetras, diccionarioLetrasNumeros)
def prioridad(cadenaNumeros,diccionarioLetras, diccionarioPalabras):
    listaPredicciones = []
    cadenaSplit = cadenaNumeros.split(" ")
    cadenaPredicciones = ''
    
    count = 0
    for cadena in cadenaSplit:
        prediccion = ''
        #Es la primera
        if count == 0:
            #Longitud mayor que 1
            if len(cadena) > 1:
                prediccion = realizaBigramUnigramPalabras('',cadena, diccionarioPalabras)
                if prediccion == '':
                    prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
                
            else:
                prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
            
        #No es la primera 
        else:
            if len(cadena) > 1:
                prediccion = realizaBigramUnigramPalabras(listaPredicciones[count - 1],cadena, diccionarioPalabras)
                if prediccion == '':
                    prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
                
            else:
                prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
        listaPredicciones.append(prediccion)    
        count = count +1
    
    
    #Obtenemos la cadena de predicciones
    for c in listaPredicciones:
        cadenaPredicciones = cadenaPredicciones + " " + c
    
    return cadenaPredicciones

def realizaBigramUnigramPalabras(palabra, cadenaNumeros, diccionarioPalabras):
    if palabra == '':
        prediccion = uniPalabras(cadenaNumeros, diccionarioPalabras)
    else:
        prediccion = biPalabras(palabra, cadenaNumeros, diccionarioPalabras)
        if prediccion == '':
            prediccion = uniPalabras(cadenaNumeros, diccionarioPalabras)

    return prediccion


def realizaBigramUnigramLetras(cadenaNumeros, diccionarioLetras):
    prediccion = ''
    anterior = ''
    prediccionActual = ''
    
    for numero in cadenaNumeros:
        if anterior == '':
            prediccionActual = uniLetras(numero, diccionarioLetras)
            prediccion = prediccion + prediccionActual
            anterior = prediccionActual
        else:
            prediccionActual = biLetras(anterior, numero, diccionarioLetras)
            prediccion = prediccion + prediccionActual
            anterior = prediccionActual
            if prediccionActual == '':
                prediccionActual = uniLetras(numero, diccionarioLetras) 
                prediccion = prediccion + prediccionActual 
                anterior = prediccionActual
                
    
    return prediccion


def uniLetras (numLetra, diccionarioLetras): #letra = número
   clavesSeleccionadas = []
   for clave in diccionarioLetras.keys():
       if clave.split('-')[0] == numLetra:
           clavesSeleccionadas.append(clave)
   
   maxClave = ''
   maxOcurrencias = 0
   for clave1 in clavesSeleccionadas:
           if diccionarioLetras[clave1].get_numOcurrencias() > maxOcurrencias:
               maxOcurrencias = diccionarioLetras[clave1].get_numOcurrencias()
               maxClave = clave1.split('-')[1]

   return maxClave


def biLetras (letraAnterior, numLetra, diccionarioLetras): #letra = número
   maxClave = ''
   maxOcurrencias = 0
   
   for clave in diccionarioLetras.keys():
       if clave.split('-')[0] == numLetra:
           diccionarioLetrasAnt = diccionarioLetras[clave].get_diccionarioPalabrasAnteriores()
           
           for claveLetrasAnt in diccionarioLetrasAnt.keys():
               if claveLetrasAnt.split('-')[1] == letraAnterior:
                   if diccionarioLetrasAnt[claveLetrasAnt] > maxOcurrencias:
                       maxClave = clave.split('-')[1]
                       maxOcurrencias = diccionarioLetrasAnt[claveLetrasAnt]
                   
   return maxClave


def uniPalabras (numerosPalabra, diccionarioPalabras): 
    clavesSeleccionadas = []
    for clave in diccionarioPalabras.keys():
        if clave.split('-')[0] == numerosPalabra:
            clavesSeleccionadas.append(clave)
    
    maxOcurrencias = 0
    maxClave = ''
    
    for clave in clavesSeleccionadas:
        if diccionarioPalabras[clave].get_numOcurrencias() > maxOcurrencias:
            maxOcurrencias = diccionarioPalabras[clave].get_numOcurrencias()
            maxClave = clave.split('-')[1]
            
    return maxClave


 
def biPalabras (palabraAnterior, numerosPalabra, diccionarioPalabras): 
    maxPrediccion = ''
    maxOcPrediccion = 0
    
    
    for clave in diccionarioPalabras.keys():
        if clave.split('-')[0] == numerosPalabra:
            diccionarioPalabrasAnt = diccionarioPalabras[clave].get_diccionarioPalabrasAnteriores()
            
            for clavePalabrasAnt in diccionarioPalabrasAnt.keys():
                if clavePalabrasAnt.split('-')[1] == palabraAnterior:
                    if diccionarioPalabrasAnt[clavePalabrasAnt] > maxOcPrediccion:
                        maxPrediccion = clave.split("-")[1]
                        maxOcPrediccion = diccionarioPalabrasAnt[clavePalabrasAnt]

                
    return maxPrediccion

def insertaPalabra(diccionarioPalabras,diccionarioLetrasNumeros, palabra, palabraAnterior):
    
    palabraCodificada = codificar(palabra,diccionarioLetrasNumeros)
    palabraAnteriorCodificada = codificar(palabraAnterior,diccionarioLetrasNumeros)
    
    #En caso de que la palabra ya esta insertada
    clave = palabraCodificada + "-" + palabra
    claveAnterior =palabraAnteriorCodificada + "-" + palabraAnterior
    if clave in diccionarioPalabras:
        entradaCorpus = diccionarioPalabras[clave]
        
        claveNumOcurrencias = entradaCorpus.get_numOcurrencias()
         
        entradaCorpus.set_numOcurrencias(claveNumOcurrencias + 1)
        
    #Palabra no esta insertada 
    else:
        eg = EstructuraGuardado(1,{})
        clave = palabraCodificada + "-" + palabra
        diccionarioPalabras[clave] = eg
        
    # Contemplamos el caso de que tuviera palabra anterior
    if palabraAnterior != '':
        entradaCorpus = diccionarioPalabras[clave]
        palabrasAnteriores = entradaCorpus.get_diccionarioPalabrasAnteriores()
        
        #En caso de que la palabra anterior ya esta insertada
        
        if claveAnterior in palabrasAnteriores:
            numOcurrencias = palabrasAnteriores[claveAnterior]
            palabrasAnteriores[claveAnterior] = numOcurrencias + 1      
        # Palabra anterior no insertada 
        else:
            palabrasAnteriores[claveAnterior] = 1
            
              
    return diccionarioPalabras

def generaDiccionarioPalabras(diccionarioPalabras,diccionarioLetrasNumeros, textoLista):
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
            diccionarioPalabras = insertaPalabra(diccionarioPalabras, diccionarioLetrasNumeros, palabra, palabraAnterior)
            
            count = count + 1
    
    
    return diccionarioPalabras
  
   
def generaDiccionarioLetras(diccionarioLetras,diccionarioLetrasNumeros, textoLista):
    letraAnterior = ''
    
    for frase in textoLista:
        
        palabras = frase.split(" ")
        palabras = eliminaElementosLongitudMenor1(palabras)
        
        for palabra in palabras:
            count = 0
            
            while (count < len(palabra)):
                letra = palabra[count]
                if count > 0:
                    letraAnterior = palabra[count - 1]
                else:
                    letraAnterior = ''
                diccionarioLetras = insertaLetra(diccionarioLetras, diccionarioLetrasNumeros, letra, letraAnterior)    
                
                count = count + 1
       

    return diccionarioLetras
    
    

   
def insertaLetra(diccionarioLetras,diccionarioLetrasNumeros, letra, letraAnterior):
    
    letraCodificada = codificar(letra,diccionarioLetrasNumeros)
    letraAnteriorCodificada = codificar(letraAnterior,diccionarioLetrasNumeros)
    
    #En caso de que la letra ya esta insertada
    clave = letraCodificada + "-" + letra
    claveAnterior = letraAnteriorCodificada + "-" + letraAnterior
    if clave in diccionarioLetras:
        entradaCorpus = diccionarioLetras[clave]
        
        claveNumOcurrencias = entradaCorpus.get_numOcurrencias()
         
        entradaCorpus.set_numOcurrencias(claveNumOcurrencias + 1)
        
    #Palabra no esta insertada 
    else:
        eg = EstructuraGuardado(1,{})
        clave = letraCodificada + "-" + letra
        diccionarioLetras[clave] = eg
        
    # Contemplamos el caso de que tuviera palabra anterior
    if letraAnterior != '':
        entradaCorpus = diccionarioLetras[clave]
        letrasAnteriores = entradaCorpus.get_diccionarioPalabrasAnteriores()
        
        #En caso de que la palabra anterior ya esta insertada
        
        if claveAnterior in letrasAnteriores:
            numOcurrencias = letrasAnteriores[claveAnterior]
            letrasAnteriores[claveAnterior] = numOcurrencias + 1      
        # Palabra anterior no insertada 
        else:
            letrasAnteriores[claveAnterior] = 1
            
               
    return diccionarioLetras
   

            
def eliminaElementosLongitudMenor1(lista):
    listaMayor1 = []
    for elem in lista:
        if len(elem) >= 1:
            listaMayor1.append(elem)
        
    return listaMayor1   
    

 
    
def codificar(palabra,diccionarioCodificacion):
    cadenaCodificada = ''
    for letra in palabra:
        for elem in diccionarioCodificacion:
            if letra in diccionarioCodificacion[elem]:
               cadenaCodificada = cadenaCodificada + elem 
               
    return cadenaCodificada


class EstructuraGuardado:
    def __init__(self, numOcurrencias, diccionarioPalabrasAnteriores):
        self.numOcurrencias = numOcurrencias
        self.diccionarioPalabrasAnteriores = diccionarioPalabrasAnteriores
        
    def get_numOcurrencias(self):
        return self.numOcurrencias
    
    def get_diccionarioPalabrasAnteriores(self):
        return self.diccionarioPalabrasAnteriores
    
    def set_numOcurrencias(self, numOcurrencias):
        self.numOcurrencias = numOcurrencias
    
    def set_diccionarioPalabrasAnteriores(self, diccionarioPalabrasAnteriores):
        self.diccionarioPalabrasAnteriores = diccionarioPalabrasAnteriores
        
    def __str__(self):
        return str(self.numOcurrencias) + "-" + str(self.diccionarioPalabrasAnteriores)

    def __repr__(self):
        return str(self.numOcurrencias) + "-" + str(self.diccionarioPalabrasAnteriores)


def main():
    diccionarios = generaDiccionarios()
    #TKinter
    textoSalida = prioridad('2671556 31132525 75 7611145 8 14 53655 732565 31141525',diccionarios[0], diccionarios[1])
    #TKinter