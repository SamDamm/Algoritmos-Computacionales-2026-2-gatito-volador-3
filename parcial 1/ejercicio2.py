#Ejercicio 2
#Samuel Cala 2251450

n = int(input("Ingrese un numero: "))

contador = 0
for num in range (2, n+1): #evaluo cada numero desde 2 hasta n para ver si es primo
    primo = True
    i = 2
    while i * i <= num : #verifico con la raiz cuadrada
        if num % i == 0: #si el residuo es 0, entonces no es primo
            primo = False 
            break
        i += 1 

    if primo:
        contador += 1

print(f"El numero de primos hasta {n} es: {contador}")