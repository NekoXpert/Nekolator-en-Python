
from NekolatorLeng  import promleng
from NekolatorComu import promComu
from NekolatorMate import promMate
from NekolatorMet import promMet
from NekolatorNTI import promNTI


#Crear un programa donde se ingrese 4 notas de un alumno y calcule su promedio final.
#Introducción
print("Bienvenido, Estimado Alumno de CERTUS, en este programa podras sacar el promedio ponderado final del ciclo.")
print("¡Empezemos!")
print("")
#Entrada
leng = round(promleng)
comu = round(promComu)
mate = round(promMate)
met = round(promMet)
nti = round(promNTI)
print("")
print("Recuerda que el promedio final de cada curso se multiplica por los creditos de cada uno de ellos. ")
print("Lenguaje (5 Creditos)")
print("Comunicación (4 Creditos)")
print("Matematicas (4 Creditos)")
print("Metodo (4 Creditos)")
print("Nuevas Tendencias (4 Creditos)")


print("")
#Proceso
PPFCX = float((leng * 5) + (comu * 4 + (mate * 4) + (met * 4)) + (nti *4))/21

PPFC = round(PPFCX, 2)

#PPFC = PROMEDIO PONDERADO FINAL DE CICLO
#Salida
print("Tu promedio final ponderado de ciclo es: ",PPFC )

#Hacer la comparación
if PPFC >= 17:
    print("¡Felicitaciones has Aprobado, Verifica si lograste una BECA!")
else:
    print("¡Buen promedio sigan asi!")
#Créditos
print("")
print("Software Creado por Nekosor")
print("Estudiante del Ciclo I de la carrera de Diseno & Desarrollo de Software")
print("Nekolator Version 1.0")
