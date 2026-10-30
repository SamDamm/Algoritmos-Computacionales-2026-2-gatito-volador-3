#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 3

#Bienvenida del usuario al programa
print("-----------------------------------------------------")
print("CÁLCULO DEL FACTOR B PARA CUADRADOS PERFECTOS")
print("-----------------------------------------------------")

#Criba de Eratóstenes para optimizar la factorización
def criba(limite):
  primos = []
  is_prime = [True] * (limite + 1)
  is_prime[0] = is_prime[1] = False
  for p in range(2, limite + 1):
    if is_prime[p]:
      primos.append(p)
      for i in range(p * p, limite + 1, p):
        is_prime[i] = False #Reconocer si el número es primo
  return primos

primos_base = criba(46341)

t_str = input("Ingrese el número de casos de prueba T: ")
if t_str.isdigit():
  T = int(t_str)
  for i in range(T):
    a_str = input(f"Ingrese el valor A para el caso {i+1}: ")
    if a_str.isdigit():
      a = int(a_str)
      b = 1
      temp = a
      for p in primos_base:
        if p * p > temp:
          break
        if temp % p == 0:
          exponente = 0
          while temp % p == 0:
            exponente += 1
            temp //= p
          if exponente % 2 != 0:
            b *= p #Calculo para determinar el cuadrado perfecto más cercano
      if temp > 1:
        b *= temp
      print(f"-> El número B más pequeño para {a} es: {b} (A*B = {a*b})")
    else:
      print("Valor inválido.") #Solo positivos y enteros
else:
  print("Error: T debe ser un número entero.")