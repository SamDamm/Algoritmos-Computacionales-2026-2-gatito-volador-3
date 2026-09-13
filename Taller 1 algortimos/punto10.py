# Taller numero 1 Algoritmos
# Samuel Ricardo Cala Herrera 2251450
# Nicolas de Jesus Gonzalez Gamboa 2251867
# 1/09/2026
# Ejercicio 10

n_valido = False
while not n_valido:
    entrada = input("Ingrese un número entero positivo n: ")
    if entrada.isdigit():
        n = int(entrada)
        if n > 0:
            n_valido = True
        else:
            print("El número debe ser mayor a 0.")
    else:
        print("Error: Debe ingresar un número entero positivo.")

primos = []
contador = 0

for num in range(2, n + 1):
    es_primo = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            es_primo = False
            break
        i += 1
        
    if es_primo:
        primos.append(num)
        contador += 1

print("\n-----------------------------------------------------")
print(f"Números primos menores o iguales a {n}:")
print(primos)
print("Cantidad total de números primos encontrados:", contador)

if contador > 0:
    print("El mayor número primo encontrado es:", primos[-1])
else:
    print("No hay números primos en el rango especificado.")