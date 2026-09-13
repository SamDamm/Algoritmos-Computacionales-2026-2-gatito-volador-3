#Taller numero 1 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#1/09/2026
#Ejercicio 6
import math as mt
print("------------------------------------------")
print("CALCULO DE LA DESVIACION ESTANDAR MUESTRAL")
print("Definicion: Se utiliza cuando solo tienes una muestra extraída de una población más grande (por ejemplo, tus mediciones repetidas en un laboratorio).")
print("Ingrese solo numeros enteros")
print("------------------------------------------")
datos = []

num = int(input("Numero elementos: "))

for _ in range(num):
    datos.append(int(input("Elemento: ")))
print("la Lista de los datos es",datos)

suma_total = 0
for x in datos:
    suma_total += x
media = suma_total / len(datos)


suma_cuadrados = 0
for x in datos:
    suma_cuadrados += (x - media) ** 2


if len(datos) > 1:
    desv_muestral = mt.sqrt(suma_cuadrados / (len(datos) - 1))
    print("La desviación estándar muestral es:", desv_muestral)
else:
    print("Error: Se necesitan al menos 2 elementos para calcular la desviación estándar muestral.")