# -*- coding: utf-8 -*-
import numpy as np
import math
"""
Created on Sat Feb 17 16:59:51 2018

@author: Ruben
"""
# ==================================================
# Conjunto de datos "Concesión de préstamos"
# Aplicaciones de Inteligencia Artificial.
# Máster en Ingeniería Informática
# ==================================================

# Contiene una serie de datos sobre concesión de préstamos en una entidad
# bancaria, en función de:

# * Tipo de empleo: funcionario, contrato laboral, parado o jubilado
# * Productos finacieros contratados en la misma entidad: 0, 1 o más de 2.
# * Propiedades inmobiliarias: 0,1 o más de 2.
# * Número de hijos: 0, 1 o más de 2.
# * Estado civil: soltero, casao, viudo, divorciado. 
# * Ingresos: bajos, medios, altos

atributos=[("Empleo",["parado", "funcionario", "laboral", "jubilado"]),
           ("Productos",["ninguno", "uno", "dos o más"]),
           ("Propiedades",["ninguna", "una", "dos o más"]),
           ("Hijos",["ninguno", "uno", "dos o más"]),
           ("Estado civil",["soltero", "casado","viudo","divorciado"]),
           ("Ingresos", ["bajos","medios","altos"])]           

# El atributo de clasificación indica si se concede o no el préstamo
# solicitado: 

clasificacion='Préstamo'

clases=['conceder','no conceder','estudiar']

# Conjuntos de entrenamiento, validación y prueba
entrenamiento=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','viudo','bajos','no conceder'],
      ['parado','dos o más','dos o más','uno','divorciado','bajos','estudiar'],
      ['funcionario','dos o más','ninguna','dos o más','divorciado','altos','conceder'],
      ['funcionario','uno','dos o más','dos o más','soltero','altos','conceder'],
      ['parado','ninguno','dos o más','dos o más','divorciado','altos','conceder'],
      ['funcionario','ninguno','ninguna','uno','viudo','altos','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','ninguno','una','uno','soltero','bajos','estudiar'],
      ['funcionario','uno','una','ninguno','divorciado','altos','conceder'],
      ['parado','dos o más','ninguna','uno','casado','bajos','estudiar'],
      ['funcionario','ninguno','una','ninguno','viudo','bajos','estudiar'],
      ['funcionario','uno','dos o más','uno','divorciado','medios','conceder'],
      ['jubilado','dos o más','dos o más','uno','divorciado','medios','conceder'],
      ['laboral','uno','dos o más','dos o más','soltero','bajos','no conceder'],
      ['jubilado','dos o más','ninguna','dos o más','divorciado','medios','no conceder'],
      ['jubilado','dos o más','una','uno','casado','medios','no conceder'],
      ['funcionario','dos o más','dos o más','uno','soltero','medios','conceder'],
      ['jubilado','uno','ninguna','uno','soltero','medios','no conceder'],
      ['funcionario','uno','dos o más','dos o más','casado','altos','conceder'],
      ['laboral','uno','ninguna','ninguno','divorciado','medios','conceder'],
      ['jubilado','ninguno','una','ninguno','divorciado','medios','estudiar'],
      ['laboral','uno','ninguna','dos o más','soltero','medios','no conceder'],
      ['parado','uno','dos o más','dos o más','soltero','bajos','conceder'],
      ['laboral','dos o más','una','ninguno','divorciado','altos','estudiar'],
      ['laboral','dos o más','ninguna','uno','viudo','bajos','estudiar'],
      ['funcionario','ninguno','dos o más','ninguno','soltero','medios','conceder'],
      ['funcionario','ninguno','una','dos o más','soltero','altos','conceder'],
      ['laboral','uno','ninguna','uno','divorciado','altos','estudiar'],
      ['jubilado','dos o más','ninguna','ninguno','soltero','altos','estudiar'],
      ['funcionario','ninguno','una','ninguno','soltero','altos','conceder'],
      ['jubilado','dos o más','ninguna','uno','casado','altos','estudiar'],
      ['laboral','dos o más','ninguna','ninguno','soltero','altos','estudiar'],
      ['jubilado','uno','dos o más','dos o más','divorciado','bajos','estudiar'],
      ['parado','uno','una','uno','divorciado','medios','estudiar'],
      ['jubilado','uno','dos o más','ninguno','soltero','medios','conceder'],
      ['jubilado','ninguno','dos o más','ninguno','casado','bajos','estudiar'],
      ['jubilado','uno','dos o más','ninguno','casado','bajos','conceder'],
      ['laboral','ninguno','dos o más','uno','casado','altos','conceder'],
      ['jubilado','uno','ninguna','uno','soltero','bajos','no conceder'],
      ['jubilado','ninguno','una','uno','viudo','altos','estudiar'],
      ['jubilado','dos o más','ninguna','uno','soltero','altos','estudiar'],
      ['funcionario','ninguno','dos o más','uno','casado','medios','conceder'],
      ['parado','uno','una','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','una','uno','casado','altos','estudiar'],
      ['laboral','uno','una','ninguno','viudo','altos','conceder'],
      ['funcionario','dos o más','una','ninguno','viudo','altos','conceder'],
      ['parado','dos o más','ninguna','ninguno','viudo','altos','conceder'],
      ['laboral','ninguno','ninguna','uno','casado','medios','estudiar'],
      ['parado','ninguno','dos o más','uno','casado','bajos','no conceder'],
      ['funcionario','ninguno','dos o más','uno','divorciado','altos','conceder'],
      ['funcionario','uno','ninguna','dos o más','divorciado','medios','estudiar'],
      ['jubilado','uno','dos o más','ninguno','soltero','bajos','no conceder'],
      ['laboral','ninguno','ninguna','ninguno','viudo','medios','estudiar'],
      ['parado','ninguno','ninguna','dos o más','casado','medios','estudiar'],
      ['jubilado','uno','una','dos o más','viudo','altos','estudiar'],
      ['funcionario','ninguno','una','uno','soltero','altos','conceder'],
      ['jubilado','dos o más','una','uno','soltero','altos','estudiar'],
      ['jubilado','dos o más','ninguna','uno','casado','medios','no conceder'],
      ['jubilado','dos o más','ninguna','uno','viudo','medios','no conceder'],
      ['parado','ninguno','una','ninguno','viudo','medios','conceder'],
      ['parado','dos o más','dos o más','ninguno','divorciado','altos','conceder'],
      ['parado','ninguno','ninguna','dos o más','viudo','medios','estudiar'],
      ['funcionario','ninguno','dos o más','dos o más','viudo','altos','conceder'],
      ['jubilado','ninguno','una','dos o más','soltero','medios','no conceder'],
      ['parado','dos o más','ninguna','uno','soltero','medios','no conceder'],
      ['funcionario','ninguno','dos o más','ninguno','soltero','altos','conceder'],
      ['laboral','uno','una','uno','soltero','bajos','no conceder'],
      ['parado','dos o más','una','dos o más','casado','bajos','no conceder'],
      ['parado','dos o más','una','uno','viudo','medios','estudiar'],
      ['laboral','uno','dos o más','ninguno','divorciado','altos','conceder'],
      ['parado','ninguno','dos o más','uno','casado','altos','estudiar'],
      ['laboral','ninguno','dos o más','dos o más','soltero','bajos','no conceder'],
      ['parado','dos o más','dos o más','dos o más','viudo','bajos','no conceder'],
      ['funcionario','uno','ninguna','ninguno','divorciado','bajos','no conceder'],
      ['jubilado','dos o más','dos o más','uno','casado','medios','conceder'],
      ['funcionario','dos o más','dos o más','ninguno','casado','altos','conceder'],
      ['parado','uno','ninguna','uno','soltero','bajos','no conceder'],
      ['jubilado','dos o más','una','dos o más','viudo','altos','estudiar'],
      ['jubilado','uno','ninguna','dos o más','casado','altos','estudiar'],
      ['jubilado','ninguno','ninguna','ninguno','viudo','bajos','no conceder'],
      ['jubilado','ninguno','una','ninguno','soltero','medios','no conceder'],
      ['parado','uno','una','dos o más','soltero','bajos','no conceder'],
      ['parado','ninguno','una','ninguno','casado','altos','estudiar'],
      ['jubilado','ninguno','ninguna','uno','soltero','medios','no conceder'],
      ['laboral','uno','dos o más','uno','casado','bajos','no conceder'],
      ['laboral','dos o más','ninguna','dos o más','soltero','bajos','estudiar'],
      ['parado','ninguno','ninguna','ninguno','soltero','medios','no conceder'],
      ['laboral','ninguno','dos o más','uno','viudo','altos','conceder'],
      ['funcionario','dos o más','ninguna','uno','casado','altos','conceder'],
      ['laboral','dos o más','una','ninguno','divorciado','bajos','estudiar'],
      ['parado','dos o más','ninguna','dos o más','soltero','altos','estudiar'],
      ['laboral','ninguno','dos o más','uno','soltero','altos','conceder'],
      ['laboral','uno','dos o más','dos o más','soltero','altos','conceder'],
      ['laboral','uno','dos o más','ninguno','viudo','bajos','no conceder'],
      ['jubilado','uno','dos o más','uno','viudo','bajos','no conceder'],
      ['jubilado','uno','dos o más','ninguno','divorciado','bajos','no conceder'],
      ['jubilado','uno','dos o más','uno','divorciado','altos','estudiar'],
      ['jubilado','uno','dos o más','uno','casado','altos','estudiar'],
      ['jubilado','ninguno','dos o más','dos o más','soltero','altos','estudiar'],
      ['funcionario','ninguno','dos o más','dos o más','viudo','bajos','estudiar'],
      ['laboral','ninguno','una','dos o más','viudo','altos','conceder'],
      ['funcionario','uno','una','uno','viudo','medios','estudiar'],
      ['parado','dos o más','ninguna','uno','casado','medios','no conceder'],
      ['parado','uno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','dos o más','dos o más','ninguno','viudo','bajos','estudiar'],
      ['funcionario','uno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['funcionario','ninguno','una','ninguno','divorciado','altos','conceder'],
      ['funcionario','ninguno','ninguna','dos o más','viudo','medios','estudiar'],
      ['laboral','ninguno','ninguna','ninguno','soltero','medios','estudiar'],
      ['jubilado','uno','dos o más','ninguno','casado','altos','estudiar'],
      ['parado','uno','una','uno','viudo','bajos','no conceder'],
      ['funcionario','ninguno','dos o más','ninguno','casado','medios','conceder'],
      ['funcionario','uno','dos o más','ninguno','soltero','medios','conceder'],
      ['parado','uno','una','ninguno','viudo','medios','estudiar'],
      ['laboral','dos o más','dos o más','dos o más','casado','bajos','estudiar'],
      ['laboral','dos o más','una','uno','soltero','medios','estudiar'],
      ['jubilado','ninguno','dos o más','dos o más','divorciado','medios','conceder'],
      ['funcionario','dos o más','dos o más','ninguno','divorciado','altos','conceder'],
      ['jubilado','dos o más','ninguna','uno','viudo','bajos','no conceder'],
      ['funcionario','dos o más','una','ninguno','soltero','bajos','estudiar'],
      ['jubilado','ninguno','una','dos o más','casado','altos','estudiar'],
      ['funcionario','uno','ninguna','ninguno','divorciado','medios','estudiar'],
      ['laboral','uno','una','ninguno','divorciado','medios','estudiar'],
      ['laboral','uno','dos o más','dos o más','soltero','medios','conceder'],
      ['funcionario','dos o más','dos o más','dos o más','viudo','medios','conceder'],
      ['parado','dos o más','ninguna','uno','divorciado','altos','estudiar'],
      ['parado','ninguno','dos o más','dos o más','soltero','altos','estudiar'],
      ['jubilado','ninguno','dos o más','dos o más','divorciado','bajos','no conceder'],
      ['parado','ninguno','dos o más','dos o más','divorciado','medios','conceder'],
      ['parado','ninguno','una','uno','viudo','altos','estudiar'],
      ['laboral','uno','una','ninguno','viudo','medios','estudiar'],
      ['laboral','ninguno','ninguna','dos o más','soltero','bajos','no conceder'],
      ['parado','ninguno','una','dos o más','divorciado','medios','no conceder'],
      ['laboral','uno','una','dos o más','casado','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','uno','casado','altos','estudiar'],
      ['parado','dos o más','una','uno','viudo','altos','estudiar'],
      ['parado','ninguno','una','ninguno','divorciado','altos','estudiar'],
      ['laboral','uno','una','dos o más','soltero','medios','estudiar'],
      ['laboral','uno','una','uno','divorciado','medios','estudiar'],
      ['parado','dos o más','ninguna','ninguno','casado','medios','no conceder'],
      ['funcionario','dos o más','ninguna','uno','casado','bajos','no conceder'],
      ['funcionario','uno','dos o más','ninguno','soltero','bajos','conceder'],
      ['parado','dos o más','ninguna','ninguno','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','ninguno','viudo','bajos','no conceder'],
      ['parado','uno','ninguna','dos o más','divorciado','bajos','no conceder'],
      ['parado','ninguno','ninguna','dos o más','divorciado','medios','no conceder'],
      ['funcionario','uno','dos o más','dos o más','casado','medios','conceder'],
      ['laboral','dos o más','una','uno','soltero','bajos','estudiar'],
      ['laboral','dos o más','dos o más','uno','viudo','altos','conceder'],
      ['jubilado','dos o más','ninguna','ninguno','casado','altos','estudiar'],
      ['jubilado','ninguno','una','ninguno','divorciado','altos','estudiar'],
      ['parado','ninguno','ninguna','uno','casado','bajos','no conceder'],
      ['parado','uno','ninguna','dos o más','soltero','bajos','no conceder'],
      ['parado','ninguno','una','uno','soltero','bajos','no conceder'],
      ['laboral','ninguno','ninguna','uno','viudo','altos','conceder'],
      ['jubilado','dos o más','una','ninguno','divorciado','bajos','no conceder'],
      ['funcionario','dos o más','ninguna','dos o más','viudo','altos','conceder'],
      ['jubilado','ninguno','ninguna','uno','viudo','altos','estudiar'],
      ['funcionario','dos o más','una','dos o más','soltero','medios','no conceder'],
      ['parado','uno','ninguna','ninguno','divorciado','medios','no conceder'],
      ['jubilado','uno','dos o más','uno','viudo','medios','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['parado','ninguno','una','ninguno','divorciado','bajos','no conceder'],
      ['funcionario','uno','dos o más','uno','viudo','altos','conceder'],
      ['jubilado','uno','una','dos o más','soltero','bajos','no conceder'],
      ['funcionario','uno','dos o más','uno','viudo','medios','conceder'],
      ['parado','dos o más','una','ninguno','soltero','altos','estudiar'],
      ['jubilado','ninguno','ninguna','ninguno','soltero','altos','estudiar'],
      ['jubilado','dos o más','dos o más','dos o más','casado','medios','conceder'],
      ['parado','dos o más','ninguna','uno','viudo','medios','no conceder'],
      ['parado','dos o más','una','uno','casado','altos','estudiar'],
      ['parado','dos o más','una','uno','divorciado','medios','estudiar'],
      ['jubilado','uno','dos o más','uno','casado','medios','conceder'],
      ['laboral','uno','dos o más','dos o más','casado','altos','conceder'],
      ['parado','ninguno','ninguna','uno','casado','medios','no conceder'],
      ['parado','ninguno','una','ninguno','soltero','altos','estudiar'],
      ['parado','ninguno','ninguna','dos o más','soltero','altos','estudiar'],
      ['parado','uno','una','uno','casado','medios','estudiar'],
      ['parado','ninguno','dos o más','uno','divorciado','bajos','no conceder'],
      ['parado','uno','dos o más','dos o más','viudo','medios','conceder'],
      ['jubilado','uno','una','dos o más','soltero','medios','estudiar'],
      ['parado','uno','ninguna','dos o más','viudo','altos','estudiar'],
      ['laboral','ninguno','una','dos o más','casado','bajos','no conceder'],
      ['jubilado','dos o más','ninguna','uno','viudo','altos','estudiar'],
      ['parado','ninguno','ninguna','uno','divorciado','bajos','no conceder'],
      ['funcionario','ninguno','ninguna','uno','divorciado','altos','conceder'],
      ['laboral','uno','una','uno','soltero','medios','estudiar'],
      ['jubilado','uno','ninguna','dos o más','soltero','medios','no conceder'],
      ['jubilado','dos o más','ninguna','dos o más','soltero','bajos','no conceder'],
      ['parado','uno','dos o más','dos o más','viudo','altos','estudiar'],
      ['parado','uno','una','uno','viudo','medios','estudiar'],
      ['funcionario','uno','dos o más','uno','casado','bajos','conceder'],
      ['laboral','uno','una','dos o más','divorciado','bajos','no conceder'],
      ['laboral','ninguno','dos o más','uno','casado','bajos','no conceder'],
      ['parado','dos o más','dos o más','ninguno','casado','medios','conceder'],
      ['parado','uno','ninguna','uno','divorciado','altos','estudiar'],
      ['laboral','uno','dos o más','uno','soltero','bajos','no conceder'],
      ['laboral','dos o más','ninguna','uno','casado','bajos','estudiar'],
      ['laboral','ninguno','ninguna','ninguno','divorciado','altos','conceder'],
      ['parado','dos o más','una','ninguno','casado','altos','estudiar'],
      ['parado','uno','una','dos o más','casado','bajos','no conceder'],
      ['funcionario','ninguno','dos o más','ninguno','soltero','bajos','conceder'],
      ['funcionario','ninguno','dos o más','uno','viudo','medios','conceder'],
      ['funcionario','dos o más','dos o más','ninguno','soltero','bajos','conceder'],
      ['parado','dos o más','ninguna','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','ninguna','dos o más','soltero','medios','no conceder'],
      ['laboral','uno','una','uno','casado','altos','conceder'],
      ['parado','dos o más','ninguna','dos o más','divorciado','bajos','no conceder'],
      ['funcionario','uno','ninguna','dos o más','divorciado','bajos','no conceder'],
      ['jubilado','uno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['laboral','uno','ninguna','dos o más','soltero','altos','conceder'],
      ['laboral','uno','una','uno','viudo','altos','conceder'],
      ['laboral','dos o más','ninguna','dos o más','soltero','medios','estudiar'],
      ['parado','ninguno','dos o más','uno','viudo','altos','estudiar'],
      ['jubilado','ninguno','ninguna','ninguno','casado','bajos','no conceder'],
      ['funcionario','dos o más','ninguna','dos o más','soltero','altos','conceder'],
      ['laboral','ninguno','dos o más','dos o más','casado','medios','conceder'],
      ['jubilado','uno','ninguna','uno','divorciado','bajos','no conceder'],
      ['parado','uno','ninguna','uno','soltero','altos','estudiar'],
      ['parado','dos o más','una','ninguno','viudo','altos','estudiar'],
      ['funcionario','ninguno','ninguna','dos o más','soltero','medios','estudiar'],
      ['parado','ninguno','una','dos o más','casado','bajos','no conceder'],
      ['funcionario','ninguno','una','ninguno','viudo','altos','conceder'],
      ['parado','dos o más','una','ninguno','viudo','medios','estudiar'],
      ['laboral','uno','una','ninguno','casado','bajos','no conceder'],
      ['parado','uno','dos o más','uno','divorciado','bajos','no conceder'],
      ['parado','dos o más','una','dos o más','viudo','bajos','no conceder'],
      ['parado','uno','ninguna','ninguno','soltero','medios','no conceder'],
      ['funcionario','dos o más','dos o más','ninguno','viudo','medios','conceder'],
      ['jubilado','dos o más','una','dos o más','divorciado','medios','no conceder'],
      ['parado','ninguno','ninguna','uno','divorciado','medios','no conceder'],
      ['funcionario','dos o más','dos o más','dos o más','soltero','altos','conceder'],
      ['jubilado','dos o más','dos o más','dos o más','viudo','bajos','no conceder'],
      ['parado','uno','ninguna','dos o más','casado','altos','estudiar'],
      ['parado','ninguno','dos o más','ninguno','soltero','bajos','no conceder'],
      ['parado','uno','dos o más','ninguno','casado','medios','conceder'],
      ['funcionario','dos o más','dos o más','uno','divorciado','medios','conceder'],
      ['funcionario','dos o más','dos o más','uno','viudo','bajos','conceder'],
      ['laboral','ninguno','una','uno','soltero','altos','conceder'],
      ['funcionario','uno','una','uno','soltero','bajos','estudiar'],
      ['funcionario','ninguno','una','ninguno','soltero','bajos','estudiar'],
      ['parado','uno','ninguna','dos o más','casado','medios','no conceder'],
      ['jubilado','uno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','ninguna','uno','viudo','bajos','no conceder'],
      ['parado','uno','dos o más','ninguno','soltero','bajos','no conceder'],
      ['laboral','dos o más','una','dos o más','soltero','bajos','estudiar'],
      ['laboral','ninguno','una','ninguno','soltero','medios','no conceder'],
      ['laboral','dos o más','dos o más','ninguno','casado','medios','conceder'],
      ['laboral','dos o más','una','ninguno','divorciado','medios','estudiar'],
      ['laboral','ninguno','dos o más','dos o más','divorciado','altos','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','casado','altos','estudiar'],
      ['parado','uno','una','uno','casado','altos','estudiar'],
      ['funcionario','dos o más','ninguna','ninguno','viudo','medios','estudiar'],
      ['laboral','uno','dos o más','uno','viudo','altos','conceder'],
      ['laboral','ninguno','ninguna','ninguno','casado','medios','estudiar'],
      ['funcionario','dos o más','ninguna','dos o más','casado','altos','conceder'],
      ['parado','uno','una','ninguno','soltero','bajos','no conceder'],
      ['funcionario','dos o más','dos o más','ninguno','casado','medios','conceder'],
      ['laboral','ninguno','ninguna','uno','divorciado','altos','conceder'],
      ['funcionario','dos o más','dos o más','uno','divorciado','altos','conceder'],
      ['laboral','uno','una','ninguno','soltero','bajos','no conceder'],
      ['funcionario','dos o más','dos o más','dos o más','viudo','bajos','conceder'],
      ['laboral','ninguno','dos o más','ninguno','divorciado','altos','conceder'],
      ['jubilado','uno','una','uno','viudo','medios','estudiar'],
      ['parado','dos o más','una','uno','casado','medios','estudiar'],
      ['laboral','ninguno','ninguna','ninguno','casado','bajos','no conceder'],
      ['laboral','uno','dos o más','dos o más','casado','medios','conceder'],
      ['funcionario','ninguno','una','uno','soltero','medios','no conceder'],
      ['funcionario','uno','dos o más','uno','casado','medios','conceder'],
      ['jubilado','dos o más','una','dos o más','casado','bajos','no conceder'],
      ['parado','dos o más','ninguna','dos o más','casado','medios','no conceder'],
      ['parado','ninguno','una','dos o más','casado','medios','no conceder'],
      ['jubilado','uno','una','ninguno','casado','medios','estudiar'],
      ['funcionario','dos o más','una','ninguno','soltero','altos','conceder'],
      ['jubilado','uno','una','dos o más','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','soltero','bajos','no conceder'],
      ['jubilado','dos o más','dos o más','ninguno','soltero','bajos','no conceder'],
      ['funcionario','dos o más','dos o más','uno','soltero','bajos','conceder'],
      ['laboral','dos o más','una','uno','divorciado','medios','estudiar'],
      ['laboral','uno','una','uno','soltero','altos','conceder'],
      ['funcionario','uno','dos o más','uno','casado','altos','conceder'],
      ['funcionario','dos o más','ninguna','uno','soltero','medios','estudiar'],
      ['funcionario','ninguno','ninguna','uno','casado','bajos','no conceder'],
      ['parado','ninguno','ninguna','uno','casado','altos','estudiar'],
      ['laboral','ninguno','una','uno','divorciado','bajos','no conceder'],
      ['parado','ninguno','ninguna','uno','divorciado','altos','estudiar'],
      ['jubilado','dos o más','dos o más','dos o más','divorciado','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','uno','viudo','medios','conceder'],
      ['laboral','dos o más','una','dos o más','divorciado','altos','conceder'],
      ['laboral','dos o más','una','uno','divorciado','altos','conceder'],
      ['funcionario','ninguno','ninguna','dos o más','divorciado','bajos','no conceder'],
      ['parado','ninguno','una','uno','casado','altos','estudiar'],
      ['jubilado','ninguno','ninguna','ninguno','soltero','bajos','no conceder'],
      ['parado','dos o más','ninguna','ninguno','divorciado','medios','no conceder'],
      ['jubilado','uno','una','ninguno','soltero','altos','estudiar'],
      ['laboral','uno','dos o más','uno','divorciado','medios','conceder'],
      ['laboral','ninguno','una','ninguno','divorciado','altos','conceder'],
      ['laboral','dos o más','dos o más','ninguno','soltero','medios','conceder'],
      ['parado','uno','dos o más','ninguno','divorciado','altos','estudiar'],
      ['parado','ninguno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','ninguno','una','ninguno','divorciado','bajos','estudiar'],
      ['laboral','ninguno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','una','ninguno','viudo','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','dos o más','casado','altos','estudiar'],
      ['jubilado','dos o más','dos o más','uno','soltero','altos','estudiar'],
      ['laboral','ninguno','dos o más','dos o más','divorciado','bajos','no conceder'],
      ['jubilado','dos o más','dos o más','ninguno','viudo','bajos','no conceder'],
      ['parado','ninguno','una','uno','viudo','medios','no conceder'],
      ['jubilado','ninguno','dos o más','uno','casado','medios','conceder'],
      ['parado','ninguno','ninguna','uno','viudo','altos','estudiar'],
      ['funcionario','uno','dos o más','dos o más','viudo','bajos','conceder'],
      ['jubilado','uno','una','ninguno','viudo','medios','estudiar'],
      ['jubilado','dos o más','una','dos o más','viudo','bajos','no conceder'],
      ['jubilado','dos o más','una','ninguno','divorciado','altos','estudiar'],
      ['laboral','dos o más','una','dos o más','viudo','medios','no conceder'],
      ['parado','dos o más','dos o más','dos o más','soltero','medios','conceder'],
      ['jubilado','uno','ninguna','ninguno','divorciado','medios','no conceder'],
      ['laboral','uno','ninguna','dos o más','casado','altos','conceder'],
      ['parado','dos o más','ninguna','ninguno','casado','bajos','no conceder'],
      ['laboral','dos o más','una','uno','soltero','altos','conceder'],
      ['laboral','ninguno','dos o más','uno','viudo','medios','conceder'],
      ['laboral','ninguno','ninguna','uno','viudo','medios','estudiar'],
      ['funcionario','ninguno','dos o más','dos o más','divorciado','bajos','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','viudo','medios','no conceder']]


validacion=[['parado','uno','ninguna','ninguno','casado','bajos','no conceder'],
       ['laboral','uno','ninguna','ninguno','viudo','medios','estudiar'],
       ['funcionario','ninguno','ninguna','ninguno','divorciado','altos','conceder'],
       ['laboral','ninguno','una','ninguno','divorciado','medios','no conceder'],
       ['parado','dos o más','una','dos o más','casado','medios','no conceder'],
       ['parado','uno','una','ninguno','divorciado','medios','estudiar'],
       ['laboral','ninguno','dos o más','dos o más','viudo','bajos','no conceder'],
       ['funcionario','dos o más','una','ninguno','viudo','bajos','estudiar'],
       ['funcionario','dos o más','una','ninguno','casado','altos','conceder'],
       ['laboral','dos o más','ninguna','dos o más','viudo','altos','conceder'],
       ['laboral','uno','ninguna','ninguno','viudo','bajos','no conceder'],
       ['funcionario','dos o más','dos o más','uno','viudo','altos','conceder'],
       ['laboral','uno','dos o más','dos o más','viudo','altos','conceder'],
       ['laboral','dos o más','una','uno','viudo','altos','conceder'],
       ['parado','uno','una','dos o más','soltero','medios','estudiar'],
       ['jubilado','ninguno','una','dos o más','viudo','bajos','no conceder'],
       ['funcionario','ninguno','dos o más','uno','divorciado','bajos','conceder'],
       ['parado','uno','una','ninguno','viudo','altos','estudiar'],
       ['parado','dos o más','una','ninguno','divorciado','bajos','no conceder'],
       ['jubilado','dos o más','una','uno','soltero','bajos','no conceder'],
       ['funcionario','ninguno','dos o más','ninguno','casado','altos','conceder'],
       ['jubilado','ninguno','ninguna','ninguno','casado','altos','estudiar'],
       ['funcionario','dos o más','una','dos o más','divorciado','medios','no conceder'],
       ['funcionario','uno','ninguna','uno','soltero','altos','conceder'],
       ['parado','dos o más','dos o más','ninguno','viudo','bajos','no conceder'],
       ['laboral','ninguno','ninguna','ninguno','divorciado','bajos','no conceder'],
       ['funcionario','dos o más','ninguna','uno','viudo','medios','estudiar'],
       ['parado','uno','una','dos o más','divorciado','bajos','no conceder'],
       ['laboral','dos o más','dos o más','uno','soltero','altos','conceder'],
       ['parado','dos o más','ninguna','ninguno','soltero','medios','no conceder'],
       ['funcionario','uno','ninguna','uno','soltero','medios','estudiar'],
       ['funcionario','ninguno','ninguna','dos o más','soltero','altos','conceder'],
       ['funcionario','uno','dos o más','ninguno','casado','medios','conceder'],
       ['funcionario','dos o más','ninguna','ninguno','divorciado','bajos','no conceder'],
       ['parado','ninguno','una','dos o más','casado','altos','estudiar'],
       ['jubilado','ninguno','ninguna','dos o más','casado','bajos','no conceder'],
       ['parado','uno','una','ninguno','casado','altos','estudiar'],
       ['laboral','dos o más','una','ninguno','soltero','medios','estudiar'],
       ['parado','ninguno','dos o más','ninguno','viudo','medios','conceder'],
       ['funcionario','uno','una','uno','casado','medios','estudiar'],
       ['laboral','uno','dos o más','ninguno','casado','medios','conceder'],
       ['jubilado','uno','una','uno','divorciado','medios','estudiar'],
       ['parado','uno','dos o más','ninguno','viudo','medios','conceder'],
       ['laboral','dos o más','ninguna','dos o más','viudo','medios','estudiar'],
       ['funcionario','ninguno','dos o más','uno','viudo','altos','conceder'],
       ['jubilado','dos o más','ninguna','ninguno','viudo','bajos','no conceder'],
       ['jubilado','uno','dos o más','uno','divorciado','bajos','no conceder'],
       ['funcionario','uno','dos o más','uno','viudo','bajos','conceder'],
       ['jubilado','dos o más','ninguna','ninguno','casado','bajos','no conceder'],
       ['jubilado','uno','una','uno','divorciado','bajos','no conceder'],
       ['laboral','ninguno','dos o más','uno','soltero','medios','conceder'],
       ['laboral','dos o más','ninguna','uno','viudo','altos','conceder'],
       ['laboral','dos o más','ninguna','uno','divorciado','altos','conceder'],
       ['jubilado','uno','ninguna','uno','casado','bajos','no conceder'],
       ['parado','dos o más','una','ninguno','soltero','medios','estudiar'],
       ['jubilado','ninguno','dos o más','uno','viudo','bajos','no conceder'],
       ['parado','dos o más','dos o más','dos o más','divorciado','medios','conceder'],
       ['jubilado','dos o más','dos o más','dos o más','casado','bajos','no conceder'],
       ['jubilado','uno','dos o más','ninguno','casado','medios','conceder'],
       ['parado','uno','dos o más','dos o más','soltero','medios','conceder'],
       ['parado','uno','dos o más','dos o más','casado','medios','conceder'],
       ['jubilado','dos o más','dos o más','uno','viudo','bajos','no conceder'],
       ['parado','ninguno','una','dos o más','soltero','altos','estudiar'],
       ['funcionario','dos o más','ninguna','ninguno','casado','medios','estudiar'],
       ['laboral','dos o más','dos o más','dos o más','casado','medios','conceder'],
       ['funcionario','uno','una','ninguno','viudo','altos','conceder'],
       ['jubilado','ninguno','una','dos o más','viudo','medios','no conceder'],
       ['jubilado','dos o más','dos o más','ninguno','soltero','medios','conceder'],
       ['parado','dos o más','dos o más','ninguno','casado','bajos','no conceder'],
       ['parado','uno','ninguna','ninguno','soltero','bajos','no conceder'],
       ['laboral','dos o más','ninguna','dos o más','divorciado','altos','conceder'],
       ['jubilado','ninguno','ninguna','uno','casado','altos','estudiar'],
       ['funcionario','uno','ninguna','ninguno','casado','bajos','no conceder'],
       ['jubilado','uno','dos o más','uno','soltero','bajos','no conceder'],
       ['jubilado','dos o más','una','ninguno','soltero','altos','estudiar'],
       ['jubilado','ninguno','dos o más','dos o más','soltero','medios','conceder'],
       ['funcionario','ninguno','una','dos o más','casado','bajos','estudiar'],
       ['jubilado','dos o más','dos o más','ninguno','divorciado','medios','conceder'],
       ['funcionario','uno','una','dos o más','soltero','bajos','estudiar'],
       ['jubilado','dos o más','ninguna','ninguno','soltero','medios','no conceder'],
       ['laboral','uno','una','dos o más','casado','altos','conceder'],
       ['laboral','dos o más','una','dos o más','soltero','medios','no conceder'],
       ['jubilado','dos o más','ninguna','ninguno','casado','medios','no conceder'],
       ['parado','ninguno','una','dos o más','viudo','altos','estudiar'],
       ['funcionario','dos o más','una','uno','divorciado','medios','estudiar'],
       ['jubilado','uno','dos o más','dos o más','viudo','bajos','no conceder'],
       ['laboral','dos o más','dos o más','dos o más','divorciado','medios','conceder'],
       ['funcionario','dos o más','una','uno','viudo','medios','estudiar'],
       ['jubilado','ninguno','una','uno','soltero','bajos','no conceder'],
       ['funcionario','dos o más','ninguna','dos o más','soltero','bajos','no conceder'],
       ['laboral','ninguno','una','ninguno','soltero','altos','conceder'],
       ['laboral','ninguno','una','ninguno','casado','altos','conceder'],
       ['jubilado','dos o más','una','uno','soltero','medios','estudiar'],
       ['funcionario','uno','ninguna','uno','viudo','bajos','no conceder'],
       ['jubilado','dos o más','una','dos o más','casado','altos','estudiar'],
       ['parado','ninguno','dos o más','dos o más','viudo','altos','estudiar'],
       ['jubilado','ninguno','dos o más','ninguno','soltero','altos','estudiar'],
       ['funcionario','ninguno','una','ninguno','casado','bajos','estudiar'],
       ['jubilado','dos o más','dos o más','dos o más','viudo','altos','estudiar'],
       ['funcionario','uno','ninguna','uno','casado','medios','estudiar'],
       ['funcionario','uno','una','dos o más','casado','medios','estudiar'],
       ['jubilado','uno','ninguna','dos o más','divorciado','medios','no conceder'],
       ['parado','dos o más','una','dos o más','soltero','bajos','no conceder'],
       ['parado','uno','dos o más','uno','viudo','medios','conceder'],
       ['jubilado','ninguno','ninguna','uno','divorciado','altos','estudiar'],
       ['funcionario','dos o más','ninguna','ninguno','soltero','medios','estudiar'],
       ['funcionario','dos o más','una','dos o más','viudo','altos','conceder'],
       ['funcionario','ninguno','dos o más','dos o más','viudo','medios','conceder'],
       ['funcionario','ninguno','ninguna','ninguno','divorciado','bajos','no conceder'],
       ['laboral','ninguno','una','uno','casado','medios','no conceder'],
       ['funcionario','ninguno','dos o más','dos o más','soltero','medios','conceder'],
       ['laboral','uno','una','uno','divorciado','bajos','no conceder'],
       ['jubilado','dos o más','ninguna','dos o más','viudo','altos','estudiar'],
       ['parado','dos o más','una','dos o más','casado','altos','estudiar'],
       ['parado','dos o más','una','dos o más','soltero','medios','no conceder'],
       ['laboral','ninguno','ninguna','dos o más','casado','altos','conceder'],
       ['laboral','ninguno','una','dos o más','viudo','medios','no conceder'],
       ['jubilado','uno','ninguna','uno','divorciado','altos','estudiar'],
       ['funcionario','dos o más','dos o más','ninguno','divorciado','medios','conceder'],
       ['funcionario','dos o más','una','uno','viudo','bajos','estudiar'],
       ['parado','uno','dos o más','ninguno','soltero','altos','estudiar'],
       ['parado','uno','ninguna','ninguno','divorciado','altos','estudiar'],
       ['laboral','ninguno','dos o más','ninguno','divorciado','bajos','no conceder'],
       ['parado','uno','dos o más','dos o más','viudo','bajos','no conceder'],
       ['laboral','dos o más','ninguna','ninguno','soltero','bajos','estudiar'],
       ['parado','ninguno','una','uno','soltero','medios','no conceder'],
       ['parado','dos o más','ninguna','ninguno','viudo','medios','no conceder'],
       ['laboral','dos o más','una','uno','casado','medios','estudiar'],
       ['jubilado','dos o más','dos o más','ninguno','soltero','altos','estudiar'],
       ['jubilado','dos o más','ninguna','dos o más','casado','altos','estudiar'],
       ['laboral','ninguno','dos o más','ninguno','soltero','bajos','no conceder'],
       ['funcionario','dos o más','ninguna','uno','divorciado','medios','estudiar'],
       ['parado','uno','ninguna','ninguno','casado','medios','no conceder'],
       ['laboral','ninguno','ninguna','ninguno','divorciado','medios','estudiar'],
       ['laboral','dos o más','una','uno','casado','altos','conceder'],
       ['parado','ninguno','dos o más','ninguno','casado','medios','conceder'],
       ['jubilado','dos o más','ninguna','uno','divorciado','medios','no conceder'],
       ['parado','ninguno','una','ninguno','divorciado','medios','no conceder'],
       ['laboral','dos o más','una','ninguno','soltero','altos','conceder'],
       ['jubilado','dos o más','dos o más','dos o más','soltero','altos','estudiar'],
       ['funcionario','dos o más','una','dos o más','soltero','bajos','estudiar'],
       ['funcionario','ninguno','una','uno','casado','medios','no conceder'],
       ['laboral','uno','una','ninguno','casado','medios','estudiar'],
       ['jubilado','uno','ninguna','dos o más','viudo','medios','no conceder'],
       ['parado','dos o más','dos o más','ninguno','soltero','altos','estudiar'],
       ['funcionario','dos o más','dos o más','uno','soltero','altos','conceder'],
       ['jubilado','uno','ninguna','uno','divorciado','medios','no conceder'],
       ['funcionario','ninguno','ninguna','uno','soltero','altos','conceder'],
       ['funcionario','dos o más','dos o más','ninguno','soltero','altos','conceder'],
       ['jubilado','uno','una','ninguno','viudo','altos','estudiar'],
       ['laboral','ninguno','ninguna','dos o más','divorciado','medios','estudiar'],
       ['parado','uno','dos o más','ninguno','viudo','altos','estudiar'],
       ['laboral','ninguno','una','uno','soltero','medios','no conceder'],
       ['laboral','uno','una','dos o más','soltero','bajos','no conceder'],
       ['laboral','dos o más','una','uno','casado','bajos','estudiar'],
       ['funcionario','uno','una','uno','viudo','altos','conceder'],
       ['parado','ninguno','dos o más','ninguno','divorciado','bajos','no conceder'],
       ['laboral','uno','ninguna','ninguno','casado','bajos','no conceder'],
       ['funcionario','ninguno','dos o más','dos o más','casado','medios','conceder'],
       ['laboral','uno','dos o más','uno','divorciado','altos','conceder'],
       ['laboral','dos o más','dos o más','uno','divorciado','bajos','estudiar'],
       ['funcionario','uno','dos o más','ninguno','viudo','bajos','conceder']]

prueba=[['funcionario','ninguno','dos o más','ninguno','divorciado','medios','conceder'],
      ['funcionario','uno','dos o más','dos o más','divorciado','bajos','conceder'],
      ['laboral','dos o más','una','ninguno','casado','medios','estudiar'],
      ['jubilado','uno','ninguna','ninguno','viudo','bajos','estudiar'],
      ['laboral','dos o más','dos o más','uno','casado','medios','conceder'],
      ['laboral','dos o más','dos o más','uno','casado','altos','conceder'],
      ['parado','ninguno','una','dos o más','divorciado','altos','estudiar'],
      ['parado','uno','dos o más','uno','casado','medios','conceder'],
      ['laboral','uno','una','uno','casado','medios','estudiar'],
      ['laboral','uno','ninguna','dos o más','divorciado','bajos','no conceder'],
      ['laboral','uno','dos o más','uno','soltero','medios','conceder'],
      ['jubilado','uno','dos o más','dos o más','casado','medios','conceder'],
      ['parado','ninguno','una','uno','viudo','bajos','no conceder'],
      ['parado','dos o más','dos o más','ninguno','viudo','altos','estudiar'],
      ['funcionario','ninguno','ninguna','ninguno','soltero','medios','estudiar'],
      ['funcionario','ninguno','una','uno','viudo','bajos','estudiar'],
      ['funcionario','ninguno','ninguna','ninguno','soltero','bajos','no conceder'],
      ['jubilado','ninguno','dos o más','ninguno','soltero','bajos','no conceder'],
      ['parado','ninguno','dos o más','ninguno','divorciado','altos','estudiar'],
      ['jubilado','dos o más','dos o más','uno','casado','bajos','no conceder'],
      ['funcionario','uno','ninguna','dos o más','viudo','altos','conceder'],
      ['laboral','uno','ninguna','ninguno','divorciado','bajos','no conceder'],
      ['laboral','uno','ninguna','dos o más','soltero','bajos','no conceder'],
      ['jubilado','ninguno','una','dos o más','soltero','bajos','no conceder'],
      ['parado','ninguno','ninguna','uno','viudo','bajos','no conceder'],
      ['funcionario','uno','ninguna','ninguno','viudo','bajos','no conceder'],
      ['parado','ninguno','dos o más','dos o más','soltero','medios','conceder'],
      ['parado','ninguno','ninguna','ninguno','soltero','altos','estudiar'],
      ['parado','ninguno','dos o más','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','ninguna','dos o más','soltero','altos','estudiar'],
      ['jubilado','uno','dos o más','ninguno','soltero','altos','estudiar'],
      ['parado','ninguno','dos o más','uno','casado','medios','conceder'],
      ['laboral','ninguno','dos o más','dos o más','casado','altos','conceder'],
      ['parado','uno','ninguna','uno','soltero','medios','no conceder'],
      ['laboral','ninguno','dos o más','ninguno','soltero','medios','conceder'],
      ['funcionario','uno','ninguna','dos o más','casado','altos','conceder'],
      ['funcionario','dos o más','dos o más','dos o más','divorciado','bajos','conceder'],
      ['jubilado','ninguno','una','dos o más','divorciado','bajos','no conceder'],
      ['parado','uno','dos o más','ninguno','soltero','medios','conceder'],
      ['jubilado','ninguno','ninguna','dos o más','viudo','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','viudo','altos','conceder'],
      ['parado','ninguno','ninguna','uno','soltero','medios','no conceder'],
      ['laboral','ninguno','una','uno','soltero','bajos','no conceder'],
      ['laboral','dos o más','una','dos o más','casado','medios','no conceder'],
      ['laboral','dos o más','ninguna','ninguno','viudo','medios','estudiar'],
      ['laboral','uno','dos o más','dos o más','divorciado','bajos','no conceder'],
      ['funcionario','uno','ninguna','dos o más','soltero','medios','estudiar'],
      ['jubilado','dos o más','ninguna','ninguno','soltero','bajos','no conceder'],
      ['jubilado','dos o más','una','ninguno','casado','bajos','no conceder'],
      ['laboral','ninguno','dos o más','dos o más','soltero','altos','conceder'],
      ['funcionario','ninguno','dos o más','uno','casado','altos','conceder'],
      ['laboral','ninguno','ninguna','uno','soltero','medios','estudiar'],
      ['laboral','uno','ninguna','dos o más','divorciado','medios','estudiar'],
      ['funcionario','dos o más','una','ninguno','casado','bajos','estudiar'],
      ['laboral','dos o más','una','ninguno','viudo','bajos','estudiar'],
      ['laboral','uno','ninguna','uno','casado','altos','conceder'],
      ['jubilado','ninguno','una','dos o más','divorciado','altos','estudiar'],
      ['laboral','dos o más','dos o más','ninguno','divorciado','altos','conceder'],
      ['jubilado','uno','ninguna','ninguno','soltero','altos','estudiar'],
      ['laboral','ninguno','dos o más','ninguno','soltero','altos','conceder'],
      ['parado','dos o más','ninguna','uno','soltero','altos','estudiar'],
      ['parado','dos o más','una','ninguno','casado','medios','estudiar'],
      ['funcionario','dos o más','dos o más','dos o más','viudo','altos','conceder'],
      ['jubilado','dos o más','una','dos o más','divorciado','bajos','no conceder'],
      ['jubilado','dos o más','dos o más','ninguno','casado','medios','conceder'],
      ['laboral','uno','ninguna','uno','soltero','medios','estudiar'],
      ['laboral','uno','una','dos o más','soltero','altos','conceder'],
      ['parado','ninguno','una','ninguno','soltero','medios','estudiar'],
      ['parado','ninguno','ninguna','dos o más','soltero','medios','no conceder'],
      ['laboral','dos o más','dos o más','dos o más','viudo','bajos','estudiar'],
      ['jubilado','dos o más','una','ninguno','viudo','medios','estudiar'],
      ['funcionario','uno','dos o más','uno','soltero','medios','conceder'],
      ['jubilado','uno','dos o más','uno','soltero','medios','conceder'],
      ['parado','ninguno','una','ninguno','viudo','altos','estudiar'],
      ['parado','dos o más','ninguna','ninguno','divorciado','bajos','no conceder'],
      ['laboral','ninguno','ninguna','uno','divorciado','medios','estudiar'],
      ['funcionario','uno','dos o más','uno','divorciado','bajos','conceder'],
      ['laboral','uno','ninguna','ninguno','soltero','bajos','no conceder'],
      ['jubilado','dos o más','ninguna','dos o más','viudo','bajos','no conceder'],
      ['jubilado','ninguno','una','dos o más','casado','bajos','no conceder'],
      ['laboral','dos o más','dos o más','dos o más','divorciado','bajos','estudiar'],
      ['parado','dos o más','dos o más','ninguno','divorciado','bajos','no conceder'],
      ['laboral','dos o más','dos o más','uno','divorciado','medios','conceder'],
      ['funcionario','uno','una','dos o más','casado','bajos','estudiar'],
      ['funcionario','uno','dos o más','ninguno','divorciado','bajos','conceder'],
      ['funcionario','dos o más','ninguna','dos o más','viudo','medios','estudiar'],
      ['laboral','ninguno','ninguna','ninguno','soltero','altos','conceder'],
      ['funcionario','ninguno','dos o más','ninguno','divorciado','bajos','conceder'],
      ['parado','dos o más','dos o más','dos o más','viudo','altos','estudiar'],
      ['jubilado','dos o más','dos o más','ninguno','casado','altos','estudiar'],
      ['parado','uno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['laboral','dos o más','una','uno','viudo','bajos','estudiar'],
      ['laboral','uno','ninguna','dos o más','viudo','medios','estudiar'],
      ['jubilado','ninguno','una','ninguno','viudo','medios','no conceder'],
      ['parado','uno','una','ninguno','casado','bajos','no conceder'],
      ['funcionario','uno','ninguna','uno','casado','altos','conceder'],
      ['laboral','ninguno','una','uno','divorciado','altos','conceder'],
      ['jubilado','uno','ninguna','ninguno','soltero','medios','no conceder'],
      ['funcionario','ninguno','dos o más','uno','soltero','altos','conceder'],
      ['laboral','ninguno','una','uno','casado','bajos','no conceder'],
      ['laboral','dos o más','dos o más','uno','casado','bajos','estudiar'],
      ['parado','uno','dos o más','ninguno','casado','altos','estudiar'],
      ['funcionario','dos o más','dos o más','dos o más','divorciado','altos','conceder'],
      ['jubilado','dos o más','una','uno','viudo','altos','estudiar'],
      ['laboral','uno','una','ninguno','viudo','bajos','no conceder'],
      ['funcionario','uno','una','uno','divorciado','altos','conceder'],
      ['jubilado','uno','ninguna','dos o más','viudo','altos','estudiar'],
      ['funcionario','ninguno','una','dos o más','soltero','medios','no conceder'],
      ['jubilado','uno','dos o más','ninguno','divorciado','altos','estudiar'],
      ['jubilado','ninguno','ninguna','ninguno','casado','medios','no conceder'],
      ['parado','ninguno','una','uno','divorciado','medios','no conceder'],
      ['laboral','ninguno','una','dos o más','casado','medios','no conceder'],
      ['jubilado','uno','dos o más','ninguno','divorciado','medios','conceder'],
      ['jubilado','ninguno','una','ninguno','soltero','bajos','no conceder'],
      ['parado','ninguno','una','ninguno','casado','medios','no conceder'],
      ['parado','uno','ninguna','uno','casado','medios','no conceder'],
      ['jubilado','uno','una','ninguno','soltero','bajos','no conceder'],
      ['parado','dos o más','dos o más','dos o más','casado','bajos','no conceder'],
      ['funcionario','ninguno','una','uno','viudo','medios','no conceder'],
      ['jubilado','dos o más','ninguna','dos o más','viudo','medios','no conceder'],
      ['jubilado','dos o más','dos o más','uno','viudo','altos','estudiar'],
      ['jubilado','dos o más','dos o más','dos o más','soltero','medios','conceder'],
      ['parado','dos o más','ninguna','uno','divorciado','bajos','no conceder'],
      ['laboral','dos o más','dos o más','ninguno','soltero','altos','conceder'],
      ['jubilado','ninguno','dos o más','dos o más','viudo','altos','estudiar'],
      ['laboral','uno','ninguna','ninguno','soltero','medios','estudiar'],
      ['jubilado','dos o más','ninguna','ninguno','viudo','medios','no conceder'],
      ['jubilado','ninguno','dos o más','uno','soltero','altos','estudiar'],
      ['funcionario','ninguno','ninguna','dos o más','casado','medios','estudiar'],
      ['jubilado','dos o más','ninguna','ninguno','divorciado','medios','no conceder'],
      ['parado','dos o más','ninguna','uno','casado','altos','estudiar'],
      ['jubilado','ninguno','una','uno','viudo','medios','no conceder'],
      ['parado','dos o más','dos o más','uno','soltero','medios','conceder'],
      ['jubilado','dos o más','dos o más','ninguno','viudo','medios','conceder'],
      ['jubilado','dos o más','una','ninguno','casado','medios','estudiar'],
      ['funcionario','uno','una','ninguno','casado','altos','conceder'],
      ['funcionario','uno','una','dos o más','casado','altos','conceder'],
      ['jubilado','ninguno','una','ninguno','casado','altos','estudiar'],
      ['funcionario','uno','una','ninguno','casado','medios','estudiar'],
      ['jubilado','uno','ninguna','ninguno','casado','altos','estudiar'],
      ['laboral','ninguno','una','dos o más','soltero','medios','no conceder'],
      ['funcionario','dos o más','una','ninguno','soltero','medios','estudiar'],
      ['parado','dos o más','ninguna','uno','viudo','bajos','no conceder'],
      ['funcionario','dos o más','una','uno','soltero','bajos','estudiar'],
      ['jubilado','ninguno','dos o más','dos o más','viudo','medios','conceder'],
      ['laboral','uno','ninguna','uno','soltero','altos','conceder'],
      ['laboral','ninguno','una','ninguno','casado','bajos','no conceder'],
      ['laboral','uno','ninguna','dos o más','viudo','bajos','no conceder'],
      ['laboral','uno','ninguna','ninguno','divorciado','altos','conceder'],
      ['parado','uno','dos o más','dos o más','divorciado','bajos','no conceder'],
      ['laboral','uno','una','uno','divorciado','altos','conceder'],
      ['funcionario','uno','una','uno','casado','bajos','estudiar'],
      ['funcionario','ninguno','una','uno','divorciado','bajos','estudiar'],
      ['laboral','uno','dos o más','dos o más','casado','bajos','no conceder'],
      ['parado','uno','ninguna','uno','divorciado','medios','no conceder'],
      ['laboral','uno','ninguna','uno','viudo','altos','conceder'],
      ['laboral','dos o más','una','ninguno','viudo','medios','estudiar'],
      ['parado','ninguno','ninguna','uno','soltero','altos','estudiar'],
      ['jubilado','ninguno','una','uno','casado','bajos','no conceder'],
      ['jubilado','uno','ninguna','uno','soltero','altos','estudiar'],
      ['parado','uno','dos o más','ninguno','divorciado','bajos','no conceder'],
      ['funcionario','uno','dos o más','ninguno','viudo','medios','conceder'],
      ['funcionario','dos o más','dos o más','dos o más','divorciado','medios','conceder']]



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
#clasificador1.imprime()
clasificador1.clasifica(['jubilado','ninguno','ninguna','uno','soltero','altos'])
clasificador1.evalua(prueba)