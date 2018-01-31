import re


def generaDiccionarios():
    '''En esta funcion se genera una tupla de dos diccionarios: Unigram y bigram de letras y unigram y bigram de palabras'''
    
    #Cuando encontremos un punto en el texto entendemos que no hay relación con la palabra anterior
    
    
    #La estructura de ambos diccionarios es la siguiente: {'claveUnigram': NumOcurrenciasUnigram-{claveBigram: NumOcurrenciasBigram}}
    #Cada clave está formada por el número correspondiente a la palabra y la palabra en sí de separadas por -. Ejemplo: 3541-hola
    #Cada valor está compuesto por Número de ocurrencias usadas para el unigram y un diccionario
    #Este diccionario usado para el bigram está compuesto por la misma estructura de la clave que antes y como valor tiene asociado el 
    #número de veces que aparece esta última clave antes de la primera clave mencionada
    
    
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
    
    # Definimos los diccionarios de letras y palabras
    #print(codificar('estamos',diccionarioLetrasNumeros))
    #print(codificar('haciendo',diccionarioLetrasNumeros))
    #print(codificar('un',diccionarioLetrasNumeros))
    diccionarioLetras = {}
    diccionarioPalabras = {}
    

    
    textoLista = []
    texto = ''
    
    #Abrimos el fichero de texto
    for line in open("prueba.txt", 'r'):
        texto = texto + line
    
    #Eliminamos los caracteres especiales y no utiles y lo formateamos
    texto = texto.lower()
    textoSinCaracteresEspeciales = re.sub('[^a-zA-Z0-9-_*. áéíóúÁÉÍÓÚüÜñÑ]', '', texto)
    textoSinCaracteresEspeciales = re.sub('[ +]', '-', textoSinCaracteresEspeciales)
    textoSinCaracteresEspeciales = re.sub('-{2,}', '', textoSinCaracteresEspeciales)
    textoSinCaracteresEspeciales = re.sub('-', ' ', textoSinCaracteresEspeciales)
    
    #Dividimos el texto por los puntos
    textoLista = textoSinCaracteresEspeciales.split(".");
    
    
    diccionarioPalabras = generaDiccionarioPalabras(diccionarioPalabras, diccionarioLetrasNumeros, textoLista)
    diccionarioLetras = generaDiccionarioLetras(diccionarioLetras, diccionarioLetrasNumeros, textoLista)
    #print(diccionarioPalabras)
    #print(diccionarioLetras)
    
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
    
    return (diccionarioLetras, diccionarioPalabras)



def prioridadBigramPalabras(cadenaNumeros,diccionarioLetras, diccionarioPalabras):
    '''En este método se predice una cadena intentando primero el bigram de palabras, sino a unigram de palabras, sino a bigram de letras y
    sino a unigram de letras'''
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





def prioridadUnigramPalabras(cadenaNumeros,diccionarioLetras, diccionarioPalabras):
    '''En este método se predice una cadena intentando primero el unigram de palabras, sino a bigram de letras y
    sino a unigram de letras'''
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
                prediccion = uniPalabras(cadena, diccionarioPalabras)
                if prediccion == '':
                    prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
                
            else:
                prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
            
        #No es la primera 
        else:
            if len(cadena) > 1:
                prediccion = uniPalabras(cadena, diccionarioPalabras)
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


def prioridadBigramLetras(cadenaNumeros,diccionarioLetras, diccionarioPalabras):
    '''En este método se predice una cadena intentando primero el bigram de letras y sino a unigram de letras'''
    listaPredicciones = []
    cadenaSplit = cadenaNumeros.split(" ")
    cadenaPredicciones = ''
    
    for cadena in cadenaSplit:
        prediccion = realizaBigramUnigramLetras(cadena,diccionarioLetras)
                
        listaPredicciones.append(prediccion)    
        
    
    #Obtenemos la cadena de predicciones
    for c in listaPredicciones:
        cadenaPredicciones = cadenaPredicciones + " " + c
    
    return cadenaPredicciones

def prioridadUnigramLetras(cadenaNumeros,diccionarioLetras, diccionarioPalabras):
    '''En este método se predice una cadena intentando el unigram de letras'''
    listaPredicciones = []
    cadenaSplit = cadenaNumeros.split(" ")
    cadenaPredicciones = ''
    
    for cadena in cadenaSplit:
        prediccion = realizaUnigramLetras(cadena,diccionarioLetras)
        listaPredicciones.append(prediccion)        
    
    #Obtenemos la cadena de predicciones
    for c in listaPredicciones:
        cadenaPredicciones = cadenaPredicciones + " " + c
    
    return cadenaPredicciones




def realizaBigramUnigramPalabras(palabra, cadenaNumeros, diccionarioPalabras):
    '''En este método se realiza el cambio de bigram a unigram de palabras según la predicción que se obtenga'''
    if palabra == '':
        prediccion = uniPalabras(cadenaNumeros, diccionarioPalabras)
    else:
        prediccion = biPalabras(palabra, cadenaNumeros, diccionarioPalabras)
        if prediccion == '':
            prediccion = uniPalabras(cadenaNumeros, diccionarioPalabras)
            
    return prediccion



def realizaBigramUnigramLetras(cadenaNumeros, diccionarioLetras):
    '''En este método se realiza el cambio de bigram a unigram de letras según la predicción que se obtenga'''
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


def realizaUnigramLetras(cadenaNumeros, diccionarioLetras):
    '''En este método se realiza el unigram de letras'''
    prediccion = ''
    
    for numero in cadenaNumeros:
        prediccion = prediccion + uniLetras(numero, diccionarioLetras)
                
    return prediccion



def uniLetras (numLetra, diccionarioLetras):
   '''En este método se realiza el unigram de letras'''
   clavesSeleccionadas = []
   maxClave = ''
   maxOcurrencias = 0
   
   for clave in diccionarioLetras.keys():
       if clave.split('-')[0] == numLetra:
           clavesSeleccionadas.append(clave)
   
   for clave1 in clavesSeleccionadas:
           if diccionarioLetras[clave1].get_numOcurrencias() > maxOcurrencias:
               maxOcurrencias = diccionarioLetras[clave1].get_numOcurrencias()
               maxClave = clave1.split('-')[1]

   return maxClave



def biLetras (letraAnterior, numLetra, diccionarioLetras):
   '''En este método se realiza el bigram de letras'''
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
    '''En este método se realiza el unigram de palabras'''
    clavesSeleccionadas = []
    maxOcurrencias = 0
    maxClave = ''
    for clave in diccionarioPalabras.keys():
        
        if clave.split('-')[0] == numerosPalabra:
            clavesSeleccionadas.append(clave)
        
    for clave in clavesSeleccionadas:
        if diccionarioPalabras[clave].get_numOcurrencias() > maxOcurrencias:
            maxOcurrencias = diccionarioPalabras[clave].get_numOcurrencias()
            maxClave = clave.split('-')[1]
            
    return maxClave

 
    
def biPalabras (palabraAnterior, numerosPalabra, diccionarioPalabras): 
    '''En este método se realiza el bigram de palabras'''
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



def insertaPalabra(diccionarioPalabras, diccionarioLetrasNumeros, palabra, palabraAnterior):
    '''En este método se realiza la inserción de un par clave-valor en un diccionario de palabras'''
    palabraCodificada = codificar(palabra,diccionarioLetrasNumeros)
    palabraAnteriorCodificada = codificar(palabraAnterior,diccionarioLetrasNumeros)
    #En caso de que la palabra ya esta insertada
    clave = palabraCodificada + "-" + palabra
    claveAnterior = palabraAnteriorCodificada + "-" + palabraAnterior
    
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



def generaDiccionarioPalabras(diccionarioPalabras, diccionarioLetrasNumeros, textoLista):
    '''En este método se crea el diccionario de las palabras a partir del corpus'''
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
  
   
    
def generaDiccionarioLetras(diccionarioLetras, diccionarioLetrasNumeros, textoLista):
    '''En este método se crea el diccionario de las letras a partir del corpus'''
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
    '''En este método se realiza la inserción de un par clave-valor en un diccionario de letras'''
    letraCodificada = codificar(letra,diccionarioLetrasNumeros)
    letraAnteriorCodificada = codificar(letraAnterior,diccionarioLetrasNumeros)
    #En caso de que la letra ya esta insertada
    clave = letraCodificada + "-" + letra
    claveAnterior = letraAnteriorCodificada + "-" + letraAnterior
    
    if clave in diccionarioLetras:
        entradaCorpus = diccionarioLetras[clave]
        claveNumOcurrencias = entradaCorpus.get_numOcurrencias()
        entradaCorpus.set_numOcurrencias(claveNumOcurrencias + 1)
    else: #Palabra no esta insertada
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
    '''En este método se realiza para eliminar de una lista los caracteres en blanco'''
    listaMayor1 = []
    
    for elem in lista:
        if len(elem) >= 1:
            listaMayor1.append(elem)
        
    return listaMayor1   
    
 
    
def codificar(palabra,diccionarioCodificacion):
    '''Este método codifica una palabra a sus correspondientes números, teniendo en cuenta en diccionario pasado como parámetro'''
    cadenaCodificada = ''
    
    for letra in palabra:
        for elem in diccionarioCodificacion:
            if letra in diccionarioCodificacion[elem]:
               cadenaCodificada = cadenaCodificada + elem 
              
    return cadenaCodificada



class EstructuraGuardado:
    '''Estructura para la manipulación de los distintos diccionarios'''
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
    # '2671556 31132525 75'
    
    
   
    
    textoSalida = prioridadBigramPalabras('716316 67222 673261',diccionarios[0], diccionarios[1])
    print(textoSalida)
    
    #ola = biPalabras('hola', '1111',diccionarios[1])
    #ola1 = uniPalabras('1111',diccionarios[1])
    #print(ola1)
    
    #TKinter