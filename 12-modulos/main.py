"""
Modulos son funcionalidades ya hechas para
reutilizar
Podemos conseguir modulos en internet y podemos crear
nustros propios modulos
"""
#Importar modulo propio
#import mimodulo
#Importando todas las funciones del modulo
from mimodulo import *

"""
print(mimodulo.holaMundo("Alexis A."))
print(mimodulo.calculadora(3, 5, False))
"""
#importando una funcion del modulo
# from mimodulo import holaMundo
print(holaMundo("Alexis A."))
print(calculadora(5, 2, True))

# Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)