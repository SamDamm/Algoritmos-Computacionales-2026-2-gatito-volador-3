#Taller numero 1 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#1/09/2026
#Ejercicio 4
import math as mt
n = int(input("Ingrese un numero entero positivo: "))

if n <= 0 :
    print("El numero debe ser mayor a 0")

numero = n
resultado = 0
posicion = 1

while n > 0 :
    digito = n % 10
   # print(digito)
    resultado = resultado + (digito * posicion)
   # print(resultado)
    posicion = posicion * 100
    n = n // 10

print(f"El numero {numero} con ceros intercalados es: {resultado} ")