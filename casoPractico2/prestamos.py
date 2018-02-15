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
entrenamiento2=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
      ['funcionario','dos o más','ninguna','uno','viudo','bajos','estudiar'],
      ['parado','dos o más','dos o más','uno','divorciado','bajos','estudiar'],
      ['funcionario','dos o más','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','uno','dos o más','dos o más','soltero','altos','estudiar'],
      ['parado','ninguno','dos o más','dos o más','divorciado','altos','estudiar'],
      ['funcionario','ninguno','ninguna','uno','viudo','altos','estudiar'],
      ['jubilado','ninguno','ninguna','dos o más','divorciado','altos','estudiar'],
      ['funcionario','ninguno','una','uno','soltero','bajos','conceder'],
      ['funcionario','uno','una','ninguno','divorciado','altos','estudiar']]
entrenamiento2ahora=[['jubilado','ninguno','ninguna','uno','soltero','altos','no conceder']]

validacion=[['parado','uno','ninguna','ninguno','casado','bajos','no conceder'],
       ['laboral','uno','ninguna','ninguno','viudo','medios','estudiar'],
       ['funcionario','ninguno','ninguna','ninguno','divorciado','altos','conceder'],
       ['laboral','ninguno','una','ninguno','divorciado','medios','no conceder'],
       ['parado','dos o más','una','dos o más','casado','medios','no conceder'],
       ['parado','uno','una','ninguno','divorciado','medios','estudiar'],
       ['laboral','ninguno','dos o más','dos o más','viudo','bajos','no conceder'],
       ['funcionario','dos o más','una','ninguno','viudo','bajos','estudiar'],
       ['funcionario','dos o más','una','ninguno','casado','altos','conceder'],
       ['laboral','dos o más','ninguna','dos o más','viudo','altos','conceder']]

prueba=[['funcionario','ninguno','dos o más','ninguno','divorciado','medios','conceder'],
      ['funcionario','uno','dos o más','dos o más','divorciado','bajos','conceder'],
      ['laboral','dos o más','una','ninguno','casado','medios','estudiar'],
      ['jubilado','uno','ninguna','ninguno','viudo','bajos','estudiar'],
      ['laboral','dos o más','dos o más','uno','casado','medios','conceder'],
      ['laboral','dos o más','dos o más','uno','casado','altos','conceder'],
      ['parado','ninguno','una','dos o más','divorciado','altos','estudiar'],
      ['parado','uno','dos o más','uno','casado','medios','conceder'],
      ['laboral','uno','una','uno','casado','medios','estudiar'],
      ['laboral','uno','ninguna','dos o más','divorciado','bajos','no conceder']]
  
"""entrenamiento=[['jubilado','ninguno','ninguna','uno','soltero','altos','estudiar'],
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
      ['jubilado','ninguno','ninguna','dos o más','viudo','medios','no conceder']]"""

"""validacion=[['parado','uno','ninguna','ninguno','casado','bajos','no conceder'],
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
       ['funcionario','uno','dos o más','ninguno','viudo','bajos','conceder']]"""

"""prueba=[['funcionario','ninguno','dos o más','ninguno','divorciado','medios','conceder'],
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
      ['funcionario','dos o más','dos o más','dos o más','divorciado','medios','conceder']]"""

# =============================================================================
def calculaDistribucion(conjuntoActual):
    dicClases = {}
    for e in clases:
        dicClases[e] = 0
    
    for elem1 in conjuntoActual:
        dicClases[ elem1[len(elem1)-1] ] += 1
    
    return dicClases



# USADA en la funcion clasifica() para obtener cuantas personas hay de cada valor del atributo y cuantas pertenecen
# a la clase dominante
def calculaAtributoMax(conjuntoActual, atributos):
  diccionarioAtributosValores = {}
  contadorPosicion = 0
  
  dicClases = calculaDistribucion(conjuntoActual)
  
  claseMaxima = max(dicClases, key=dicClases.get)
  
  for atr in atributos:
      listaValoresAtributo = atr[1]
      dic = {}
      
      for atrVal in listaValoresAtributo:
          dic[atrVal] = [0,0]
      
      diccionarioAtributosValores[contadorPosicion] = dic
      contadorPosicion = contadorPosicion + 1
  
  for entrada in conjuntoActual:
      contadorPosicion = 0
      clase = entrada[len(entrada) - 1]
      for elem in entrada[0:len(entrada) - 1]:
          dic = diccionarioAtributosValores[contadorPosicion]
          dic[elem][0] += 1
          if clase == claseMaxima:
              dic[elem][1] += 1
          contadorPosicion += 1
             
  return diccionarioAtributosValores



def compruebaCasoBase(conjuntoInicio, conjuntoActual, cotaMinima=0, cotaMayoria=1):
    casoBase = 0
    primero = conjuntoActual[0][len(conjuntoActual[0])-1]
    #print ("primero: " + primero)
    
    # CASOS BASE:
    #  - Cuando todos los datos son de la misma clase
    for elem in conjuntoActual:
        if elem[len(elem)-1] == primero:
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
    dicClase = calculaDistribucion(conjuntoActual)
    print (dicClase)
        
    elemsMax = max(dicClase.values()) / len(conjuntoActual)
    #print (elemsMax)
    
    if elemsMax > cotaMayoria:
        casoBase = 1
    
    #CASOS EN LOS QUE SE HAN DE CREAR HOJAS:
    #   Si se queda el conjunto con un ejemplo se devuelve una hoja con la clase mayoritaria
    #   Si el conjunto está vacío se devuelve una hoja con la clase mayoritaria del nodo anterior
    if len(conjuntoActual) <= 1: 
        casoBase = 1
        
    # Si se queda sin atributos
    if len(atributos) == 0:
        casoBase = 1
    
    return casoBase
    


def aprendizajeArbolesDecision(conjuntoInicio, atributos, funcionClasificacion, cotaMinima=0, cotaMayoria=1):
    #conjuntoActual y atributosRestantes son listas de indices
    conjuntoActual = conjuntoInicio[:]
    atributosRestantes = atributos[:]
    aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes)



def aprendizajeRecursivo(conjuntoInicio, atributos, cotaMinima, cotaMayoria, funcionClasificacion, conjuntoActual, atributosRestantes):

    # Crear parametro para almacenar la clase del nodo anterior y pasarsela al nodo hoja cuando no hay mas elementos, compruebaCasoBase=0
    # Si es caso base se construye un nodo hoja
    if compruebaCasoBase(conjuntoInicio, conjuntoActual, cotaMinima, cotaMayoria) == 1:
        if len(conjuntoActual) == 1:
            nodoHoja = NodoDT(distr=calculaDistribucion(conjuntoActual),
                              atributo=None,
                              ramas=None,
                              clase=conjuntoActual[0][len(conjuntoActual[0])-1])
            #print ("nodoHoja:" + str(conjuntoActual[0][len(conjuntoActual[0])-1]))
        """elif len(conjuntoActual) == 0:
            nodoHoja = NodoDT(distr=calculaDistribucion(conjuntoActual),
                              atributo=None,
                              ramas=None,
                              clase="""
            #print ("nodoHoja:" + str(conjuntoActual[0][len(conjuntoActual[0])-1]))
    else:
        # Si no es caso base se elige el mejor atributo atr(mejor atributo) usando la funcion clasifica(funcionClasificacion), dentro se ponen los distintos sumatorios de Entropia y los otros
        nuevaClasificacion = Clasificador(funcionClasificacion, clases, atributosRestantes, conjuntoActual)
        #print ("antes")
        mejorAtributo = nuevaClasificacion.clasifica(funcionClasificacion)
        #print ("despues")
        #print("atributosAntes:" + str(atributos) )
        #print("atributosRestantesAntes:" + str(atributosRestantes) )
        # Se crea un nuevo conjuntoActual conforme al valor del atributo elegido
        ''' for en el que en cada iteracion se crea un conjunto con los elementos del conjunto actual que tengan el valor del atributo'''
        for valor in atributosRestantes[mejorAtributo][1]:
            nuevoConjuntoActual = []
            #print("valor: " + str(valor))
            for fila in conjuntoActual:
                #print("fila: " + str(fila))
                if valor == fila[mejorAtributo]:
                    nuevoConjuntoActual.append(fila)
            
            #print ("conjActual:" + str(nuevoConjuntoActual))
            
            # Se construye un nodo internmedio con distr, atr, ramas{valorAtributo: aprendizajeRecursivo(
            #       conjuntoInicio, atributos, porcentajeMinimo, porcentajeMayoria, nuevoConjuntoActual,
            #       atributosRestantes-atr)}
            atribRestantes = atributosRestantes[:]
            del(atribRestantes[mejorAtributo])
            #print("atributosDespues:" + str(atributos) )
            #print("atributosRestantesDespues:" + str(atribRestantes) )
            
            
            # No hacer llamadas recursivas sin ejemplos
            if len(nuevoConjuntoActual) > 0:
                """nuevoNodo = NodoDT(distr=calculaDistribucion(nuevoConjuntoActual),
                                   atributo=mejorAtributo,
                                   ramas={valor: aprendizajeRecursivo(entrenamiento, atributos, 0, 1, "error", nuevoConjuntoActual, atribRestantes)},
                                   clase=None)"""
            #else:#Creo una hoja con la clase anterior
    
    
    
    
    
    
    
    
    
    
    
    
    #1. Crear un nodo raiz conteniendo el conjunto inicial de entrenamiento D
    #2. REPETIR (hasta que no haya mas candidatos a nodos internos)
        #2.1 SELECCIONAR un nodo candidato a nodo interno
        #2.2 ELEGIR un criterio de decision
        #2.3 Crear los descendientes con los datos del nodo candidato que satisfacen el correspondiente valor del criterio de decision
    #3. ETIQUETAR cada nodo hoja con la clase dominante en los datos de dicho nodo (si no tiene datos, se usa la clase dominante en los datos del nodo padre)
    #4. PODAR nodos para evitar sobreajuste
    
    

class NodoDT(object):
    def __init__(self,atributo=-1,distr=None,ramas=None,clase=None):
        self.distr=distr # Diccionario con el numero de ejemplos de cada clase
        self.atributo=atributo # Indice del atributo, solo para  nodos internos
        self.ramas=ramas # Diccionario con tantas claves como valores tenga el atributo (valor del atributo: nodo inferior)
        self.clase=clase # Solo para nodos hojas
    
    
    
class Clasificador:
    def __init__(self,clasificacion,clases,atributos, conjuntoActual):
        self.clasificacion=clasificacion
        self.clases=clases
        self.atributos=atributos
        self.conjuntoActual=conjuntoActual
        
    def entrena(self,entrenamiento,validacion=None):
        pass
    
    def clasifica(self, ejemplo):
        result = ""
        dic = calculaAtributoMax(self.conjuntoActual, self.atributos)
        instanciasClaseMaxima = max(calculaDistribucion(self.conjuntoActual))
        #print ("iteracion: "+str(dic))
        
        
        # Calcular la impureza del nodo padre y restarla al sumatorio de ni/n * impureza de cada valor del atributo
        # Padre {'conceder': 6, 'no conceder': 2, 'estudiar': 7} --> - 6/15*log2(6/15) - 2/15*log2(2/15) - 7/15*log2(7/15)
        
        #print("antes de error")
        # Se hacen los sumatorios con los valores de cada atributo y quedarnos con el menor para "error"
        if ejemplo == "error":
            #print("entra en error")
            tam = len(self.conjuntoActual)
            indiceAtributoMaximo = 0
            valorErrorMinimo = 1.0
            for elem in range(len(atributos)):
                error = 0.00
                
                for elem1 in dic[elem]:
                    #print(str(elem1))
                    
                    if dic[elem][elem1][0] > 0:
                        pd = dic[elem][elem1][0]
                        si = dic[elem][elem1][1]
                        
                        error += (pd/tam)*(1 - (si/pd))
                        
                #print("atributo nuevo:"+str(error))
                if error < valorErrorMinimo:
                    valorErrorMinimo = error
                    indiceAtributoMaximo = elem
            #print(indiceAtributoMaximo)
            return indiceAtributoMaximo
                
            
        """elif ejemplo == "gini":
        else ejemplo == "entropia":
        """
        return result
    
    def evalua(self,prueba):
        pass
    
    def imprime(self):
        pass

