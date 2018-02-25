import re

# ==================================================
# Conjunto de datos "Titanic"
# Aplicaciones de Inteligencia Artificial.
# Máster en Ingeniería Informática

# ==================================================
# Contiene una serie de datos sobre el viaje del titanic, en función de:
"""
TOTALIDAD DE ATRIBUTOS:
- pclass: clase en la que viaja el sujeto.
- survived: 1: sobrevive, 0: no sobrevive.
- name: nombre del pasajero.
- age: edad del pasajero.
- embarked: ciudad de origen del pasajero.
- home.dest: ciudad de destino del pasajero.
- room: camarote del pasajero.
- ticket: numero de ticket del pasajero.
- boat: barca donde el pasajero se monto.
- sex: sexo del pasajero.
"""



def obtenerDatos ():
    textoLista = []
    
    # Saco los datos del archivo txt y los almaceno en una variable
    [ [ [ textoLista.append(line[:-1]) ] if line[-1]=='\n' else textoLista.append(line) ] for line in open("titanic.txt", 'r') ]
    
    # Modifico la lista de datos para rellenar los elementos vacios
    listaSeparaValores = separaValores(textoLista[1:])
    diccionarioEdades = calculaEdad (listaSeparaValores)
    ciudadOrigenMax = calculaElementoMaximo (listaSeparaValores, 5)
    ciudadDestinoMax = calculaElementoMaximo (listaSeparaValores, 6)
    camaroteMax = calculaElementoMaximo (listaSeparaValores, 7)
    ticketMax = calculaElementoMaximo (listaSeparaValores, 8)
    boteMax = calculaElementoMaximo (listaSeparaValores, 9)
    
    listaDatosModificada = modificaListaDatos(listaSeparaValores, diccionarioEdades, ciudadOrigenMax,
                                                  ciudadDestinoMax, camaroteMax, ticketMax, boteMax)
    
    # Devuelve los nombres de los atributos, los valores de los mismos y las edades de los vivos y los fallecidos
    return [textoLista, listaDatosModificada]
    



# Crea una lista cuyos elementos son listas contenedoras de los datos de cada persona
def separaValores (textoLista):
    res = []
    patron = []
    patron.append(re.compile('",'))
    patron.append(re.compile(',"'))
    patron.append(re.compile('"'))
    
    # Para cada persona de la lista de datos
    for i in range(len(textoLista)) :
    
        for p in range(len(patron)):
            iterador = re.finditer(patron[p], textoLista[i])
            
            for cad in iterador:
                if p == len(patron)-1:
                    textoLista[i]=textoLista[i].replace(textoLista[i][cad.start():cad.end()], "")
                    textoLista[i] += (" ")
                    break
                
                else:
                    textoLista[i]=textoLista[i].replace(textoLista[i][cad.start():cad.end()], "--")
                    
        textoLista[i] = textoLista[i].strip()
        textoLista[i] = textoLista[i].split("--")
        
        for ele in textoLista[i]: # Elimino caracteres extranios
            if textoLista[i].index(ele) == 4:
                textoLista[i][4] = textoLista[i][4].split('.')[0].strip()
                
            elif textoLista[i].index(ele) == 7:
                textoLista[i][7] = textoLista[i][7].replace("-", "").replace("(", "").replace(")", "")
                if textoLista[i][7] == "D?":
                    textoLista[i][7] = "D38"
                elif textoLista[i][7] == "B?":
                    textoLista[i][7] = "D49"
                elif textoLista[i][7] == "E?":
                    textoLista[i][7] = "D77"
                elif textoLista[i][7] == "F?":
                    textoLista[i][7] = "F33"
                textoLista[i][7] = textoLista[i][7].replace("?", "")
                
            elif textoLista[i].index(ele) == 9:
                textoLista[i][9] = textoLista[i][9].replace("(", "").replace(")", "")
                
        res.append(textoLista[i])
    
    return res



# Calcula la media de edad de los pasajeros y modifica los números por "niño" o "adulto"
# dependiendo de si son menores o mayores que 13
def calculaEdad (listaSeparaValores):
    res = {}
    totalVivos = 0
    edadesVivos = 0
    totalFallecidos = 0
    edadesFallecidos = 0
    
    for fila in range(len(listaSeparaValores)):
        
        # Personas vivas
        if int(listaSeparaValores[fila][2]) == 1 and listaSeparaValores[fila][4] != 'NA': 
            edadesVivos += int(listaSeparaValores[fila][4])
            totalVivos += 1
        
        else: # Personas fallecidas
            if listaSeparaValores[fila][4] != 'NA':
                edadesFallecidos += int(listaSeparaValores[fila][4])
                totalFallecidos += 1
    
    # Se rellena el diccionario con {'1': mediaVivos, '0': mediaFallecidos}
    mediaVivos = edadesVivos/totalVivos
    mediaFallecidos = edadesFallecidos/totalFallecidos
    
    if int( mediaVivos ) <= 13:
        res["1"] = "niño"
    else:
        res["1"] = "adulto"
    
    if int( mediaFallecidos ) <= 13:
        res["0"] = "niño"
    else:
        res["0"] = "adulto"
    
    #print("dicCalculaEdad:" + str(res) + "\n")
    return res


# Metodo que obtiene el valor de clasificacion de la clase que mas aparece
def obtenClaveMaximaPorValor (diccionarioCiudades):
   max_value = 0
   
   for key in diccionarioCiudades:
       
       if max_value is None or max_value < diccionarioCiudades[key]:
           max_value = diccionarioCiudades[key]
           max_key = key  
           
   return max_key



def calculaElementoMaximo (listaSeparaValores, indice):
    diccionarioElementos = {}
    
    for fila in range(len(listaSeparaValores)):
        
        if len(listaSeparaValores[fila][indice]) != 0:
            
            if listaSeparaValores[fila][indice] not in diccionarioElementos.keys():
                diccionarioElementos[listaSeparaValores[fila][indice]] = 1
                
            else:
                diccionarioElementos[listaSeparaValores[fila][indice]] += 1
    
    #print ("diccionarioElementos:" + str(diccionarioElementos))
    elementoMasRepetido = obtenClaveMaximaPorValor(diccionarioElementos)
    #print ("res:" + str( elementoMasRepetido ))
    
    return elementoMasRepetido



# Modifica los valores de edades a niño o adulto e introduce valores en los elementos vacios
def modificaListaDatos (listaSeparaValores, diccionarioEdades, ciudadOrigenMax, ciudadDestinoMax,
                        camaroteMax, ticketMax, boteMax):
    for fila in range(len(listaSeparaValores)):
        posicion = 0
        
        for elem in listaSeparaValores[fila]:
            
            if posicion == 4: # Edad del pasajero
                
                if (len(elem) == 0) or (elem == 'NA'): # Si el campo edad no tiene valor
                    if int(listaSeparaValores[fila][2]) == 1:
                        listaSeparaValores[fila][4] = diccionarioEdades["0"]
                    else:
                        listaSeparaValores[fila][4] = diccionarioEdades["1"]
                        
                else:
                    if int(elem) <= 13:
                        listaSeparaValores[fila][4] = "niño"
                    else:
                        listaSeparaValores[fila][4] = "adulto"
            
            elif posicion == 5: # Ciaudad de origen del pasajero
                
                if (len(elem) == 0) or (elem == 'NA'):
                    listaSeparaValores[fila][5] = ciudadOrigenMax
            
            elif posicion == 6: # Ciudad de destino de los pasajeros
                
                if (len(elem) == 0) or (elem == 'NA'):
                    listaSeparaValores[fila][6] = ciudadDestinoMax
            
            elif posicion == 7: # Camarote de los pasajeros
                
                if (len(elem) == 0) or (elem == 'NA'):
                    listaSeparaValores[fila][7] = camaroteMax
            
            elif posicion == 8: # Numero de ticket de los pasajeros
                
                if (len(elem) == 0) or (elem == 'NA'):
                    listaSeparaValores[fila][8] = ticketMax
                    
            elif posicion == 9: # Botes donde los pasajeros se montaron
                
                if (len(elem) == 0) or (elem == 'NA'):
                    listaSeparaValores[fila][9] = boteMax
                
            posicion += 1
            
    return listaSeparaValores



# Crea la lista de atributos
def listarValoresPorAtributo (listaSeparaValores):
    res = []
    lista1 = []
    lista2 = []
    lista3 = [] 
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []
    lista9 = []
    lista10 = []
    
    for fila in range(len(listaSeparaValores)):
        #print(str("FILA: " + str(listaSeparaValores[fila])))
        posicion = 0
        
        #Se ha de meter cada elemento en la lista de la posicion de la lista donde corresponda
        for elem in listaSeparaValores[fila]:
            if posicion == 1 and elem not in lista1 and len(elem) != 0:
                lista1.append(elem)
                
            elif posicion == 2 and elem not in lista2 and len(elem) != 0:
                lista2.append(elem)
                
            elif posicion == 3 and elem not in lista3 and len(elem) != 0:
                lista3.append(elem)
                
            elif posicion == 4 and elem not in lista4 and len(elem) != 0:
                lista4.append(elem)
                    
            elif posicion == 5 and elem not in lista5 and len(elem) != 0:
                lista5.append(elem)
                
            elif posicion == 6 and elem not in lista6 and len(elem) != 0:
                lista6.append(elem)
                
            elif posicion == 7 and elem not in lista7 and len(elem) != 0:
                lista7.append(elem)
                
            elif posicion == 8 and elem not in lista8 and len(elem) > 1:
                lista8.append(elem)
                
            elif posicion == 9 and elem not in lista9 and len(elem) != 0:
                lista9.append(elem)
                
            elif posicion == 10 and elem not in lista10 and len(elem) != 0:
                lista10.append(elem)
                
            posicion += 1
            
    res.append(lista1)
    res.append(lista2)
    res.append(lista3)
    res.append(lista4)
    res.append(lista5)
    res.append(lista6)
    res.append(lista7)
    res.append(lista8)
    res.append(lista9)
    res.append(lista10)
    
    return res


def obtenerAtributos (textoLista, listaDatosModificada):
    atributos = []
    resAtributos = []
    nombresAtributos = []
    listas = []
    
    # Obtengo los atributos
    listas = listarValoresPorAtributo(listaDatosModificada)
    #print("listas: " + str(listas))
    
    # Creo la lista de los nombres de los atributos
    [ [ nombresAtributos.append(atributo[1:-1]) ] for atributo in textoLista[0].split(",") ]
    #print(str(nombresAtributos))
    
    for i in range(11):
        if i > 0:
            tupla = (nombresAtributos[i], listas[i-1])
            atributos.append(tupla)
            
    #[ print(str(atributo)) for atributo in atributos ] # Lista de todos los atributos
    
    for atributo in atributos:
        if (atributo[0] == "pclass") or (atributo[0] == "room") or (atributo[0] == "boat"):
            resAtributos.append(atributo)
        elif (atributo[0] == "survived"):
            clases = atributo[1]
    #[ print(str(atributo)) for atributo in resAtributos ]
    
    return resAtributos, clases



def obtenerListas (listaDatos):
    copiaDatos = listaDatos[:]
    datosEntrenamiento = []
    datosValidacion = []
    datosPrueba = []
    
    tam = len(listaDatos)
    numDatosEntrenamiento = int(60*tam/100) # Numero de datos que contendra la lista de entrenamiento
    numDatosValidacionPrueba = int(20*tam/100) # Numero de datos que contendran las listas de validacion y prueba
    vivosFallecidos = numVivosFallecidos(listaDatos)
    #print(str(numDatosEntrenamiento) + " " + str(numDatosValidacionPrueba) + " vivosFallecidos: " + str(vivosFallecidos))
    
    contVivos = 0
    contFallecidos = 0
    for persona in listaDatos:
        #print("persona:" + str(persona))
        if persona[2] == '1':
            
            if contVivos < int(numDatosValidacionPrueba/2):# and persona not in copiaDatos:
                datosValidacion.append(persona)
                #print("dval:" + str(datosValidacion))
                copiaDatos.remove(persona)
                contVivos += 1
            
            elif contVivos < int(numDatosValidacionPrueba):# and persona not in copiaDatos:
                datosPrueba.append(persona)
                copiaDatos.remove(persona)
                contVivos += 1
        
        else:
            if contFallecidos < int(numDatosValidacionPrueba/2):# and persona not in copiaDatos:
                datosValidacion.append(persona)
                copiaDatos.remove(persona)
                contFallecidos += 1
            
            elif contFallecidos < int(numDatosValidacionPrueba):# and persona not in copiaDatos:
                datosPrueba.append(persona)
                copiaDatos.remove(persona)
                contFallecidos += 1
    
    datosEntrenamiento = copiaDatos[:]
    """print("entr: " + str(len(datosEntrenamiento)))
    print("val:" + str(len(datosValidacion)))
    print("pr: " + str(len(datosPrueba)))"""
    return [datosEntrenamiento, datosValidacion, datosPrueba]        



# Lista con el numero de vivos y fallecidos
def numVivosFallecidos (listaDatos):
    res = []
    vivos = 0
    fallecidos = 0
    
    for persona in listaDatos:
        if persona[2] == '1':
            vivos += 1
        else:
            fallecidos += 1
            
    res.append(vivos)
    res.append(fallecidos)
    
    return res



if __name__ == "__main__":
    lista = obtenerDatos()
    
    resAtr = obtenerAtributos(lista[0], lista[1])
    atributos = resAtr[0]
    clases = resAtr[1]
    
    resListas = obtenerListas(lista[1]) # lista[1] contiene la lista de todos los datos
    entrenamiento = resListas[0]
    validacion = resListas[1]
    prueba = resListas[2]

    """print("ATRIBUTOS: " + str(atributos))
    print("CLASES: " + str(clases))
    print("ENTRENAMIENTO: " + str(entrenamiento))
    print("VALIDACION: " + str(validacion))
    print("PRUEBA: " + str(prueba))"""
    
    














# * Tipo de empleo: funcionario, contrato laboral, parado o jubilado
# * Productos finacieros contratados en la misma entidad: 0, 1 o más de 2.
# * Propiedades inmobiliarias: 0,1 o más de 2.
# * Número de hijos: 0, 1 o más de 2.
# * Estado civil: soltero, casao, viudo, divorciado. 
# * Ingresos: bajos, medios, altos
"""
atributos=[("Empleo",["parado", "funcionario", "laboral", "jubilado"]),
           ("Productos",["ninguno", "uno", "dos o más"]),
           ("Propiedades",["ninguna", "una", "dos o más"]),
           ("Hijos",["ninguno", "uno", "dos o más"]),
           ("Estado civil",["soltero", "casado","viudo","divorciado"]),
           ("Ingresos", ["bajos","medios","altos"])]
"""     

# El atributo de clasificación indica si se concede o no el préstamo
# solicitado: 
"""
clasificacion='Préstamo'

clases=['conceder','no conceder','estudiar']
"""

# Conjuntos de entrenamiento, validación y prueba
"""
entrenamiento=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
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
"""