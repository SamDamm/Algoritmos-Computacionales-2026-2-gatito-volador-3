# Taller numero 1 Algoritmos
# Samuel Ricardo Cala Herrera 2251450
# Nicolas de Jesus Gonzalez Gamboa 2251867
# 1/09/2026
# Ejercicio 9
import math as mt

tolerancia = float(input("Ingrese la tolerancia epsilon: "))

suma_leibniz = 0.0
n = 0
signo = 1
termino = 1.0 

while abs(termino) >= tolerancia:
    denominador = 2 * n + 1
    termino = signo * (1.0 / denominador)
    suma_leibniz += termino
    signo *= -1
    n += 1

pi_aproximado = suma_leibniz * 4
error = abs(pi_aproximado - mt.pi)

print("\n-----------------------------------------------------")
print(f"Resultados para la tolerancia {tolerancia}:")
print("Valor aproximado de pi:", pi_aproximado)
print("Número de términos utilizados:", n)
print("Error respecto a math.pi:", error)
