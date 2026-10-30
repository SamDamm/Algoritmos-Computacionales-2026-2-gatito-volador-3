#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 2

import math

#Bienvenida del usuario al programa
print("-----------------------------------------------------")
print("PERMUTACIONES DE UNA CADENA TRAS ELIMINAR REPETIDOS")
print("-----------------------------------------------------")

cadena_entrada = input("Ingrese la cadena de caracteres: ") #Frase
n_str = input("Ingrese el número de elementos N a tomar: ") #número de salidas


if n_str.isdigit():
  N = int(n_str)
  vistos = set() #Limpieza de caracteres repetidos
  limpia = [] 
  for c in cadena_entrada:
    if c not in vistos:
      vistos.add(c)
      limpia.append(c)
  limpia.sort()
  conjunto_limpio = "".join(limpia)
  M = len(conjunto_limpio)

  if 1 <= N <= M:
    print(f"\nConjunto limpio (M={M} caracteres): {conjunto_limpio}")
    print("Generando ordenamientos lexicográficos:\n")

    def generar_permutaciones(conjunto, n, actual=""):
      if len(actual) == n:
        print(actual)
        return 1
      total = 0
      for i in range(len(conjunto)):
        siguiente_conjunto = conjunto[:i] + conjunto[i + 1 :]
        total += generar_permutaciones(conjunto[:i] + conjunto[i + 1 :], n, actual + conjunto[i])
      return total

    total_generadas = generar_permutaciones(conjunto_limpio, N)
    esperado = math.perm(M, N)
    print(f"Líneas generadas: {total_generadas} | Esperado por fórmula: {esperado}")
  else:
    print(f"Error: N debe estar entre 1 y {M}.") #Cumplimiento de la desigualdad propuesta
else:
  print("Error: Ingrese un número entero válido para N.") #Para que solo reconozca números positivos y enteros