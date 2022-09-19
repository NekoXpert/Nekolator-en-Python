#Crear un programa donde se ingrese 4 notas de un alumno y calcule su promedio final.
#Introducción
print("Bienvenido, Estimado Alumno de CERTUS, en este programa podras sacar el promedio final del curso Nuevas Tendencias.")
print("¡Empezemos!")
print("")
#Entrada
nota1 = float(input("Ingresa tu primera Nota: "))
nota2 = float(input("Ingresa tu segunda Nota: "))
nota3 = float(input("Ingresa tu tercera Nota: "))
nota4 = float(input("Ingresa tu cuarta Nota: "))
print("")
print("Recuerda que las Notas tienen los siguientes pesos: ")
print("Primera Nota un 15 %")
print("Segunda Nota un 20 %")
print("Tercera Nota un 30 %")
print("Cuarta Nota un 35 %")
print("")
#Proceso
promNTI = float((nota1*0.15) + (nota2*0.20) + (nota3*0.30) + (nota4*0.35))

#Salida
print("Tu promedio final es: ",promNTI)

#Hacer la comparación
if promNTI >= 13:
    print("¡Felicitaciones has Aprobado, ahora si date ese gustito!")
else:
    print("¡Lo lamento pero.. No Aprobado.. Sigue intentando..!")
#Créditos
print("")
print("Software Creado por Nekosor")

print("")
print("Nekolator Version 1.0")
