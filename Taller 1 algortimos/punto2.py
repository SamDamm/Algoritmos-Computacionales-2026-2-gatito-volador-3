#Taller numero 1 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#1/09/2026
#Ejercicio 2
import math as mt
b = int(input("Ingrese un numero base (b) menor que 10 y mayor o igual a 2: "))
n = int(input("Ingrese un numero (n) positivo entero mayor a 1: "))

if n <= 0:
    print("El numero (n) debe ser mayor a 0")
    n = int(input("Ingrese nuevamente un numero (n) positivo entero mayor a 1: "))

if b <= 2 or b >= 9:
    print("El numero base (b) debe ser mayor a 2 y menor que 10")
    b = int(input("Ingrese nuevamente un numero base (b) menor que 10 y mayor o igual a 2: "))

numero = n
base_b = 0
posicion = 1

while n > 0:
    residuo = n % b
    base_b = base_b + (residuo * posicion)
    posicion = posicion * 10
    n = n//b

print(f"El numero {numero} en base {b} es: {base_b} ")
