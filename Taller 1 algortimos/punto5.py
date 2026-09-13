#Taller numero 1 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#1/09/2026
#Ejercicio 5
A = []

num = int(input("Numero elementos: "))

for _ in range(num):
    A.append(int(input("Elemento?: ")))

pares = [x for x in A if x % 2 == 0]
impares = [y for y in A if y % 2 == 1]

print(A)
print(pares)
print(impares)

prompar = sum(pares) / len(pares)
proimpar = sum(impares) / len(impares)

print(f"El promedio de los pares es: {prompar}")
print(f"El promedio de los impares es: {proimpar}")
