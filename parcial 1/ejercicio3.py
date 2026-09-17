#Ejercicio 3
#Samuel Cala 2251450

n = int(input("Ingrese el número de términos de la serie de Fibonacci que no sea cero: "))

a = 0 #definimos dos variables para almacenar los datos de la serie de Fibonacci
b = 1
contador_pares = 0

for i in range(n) : #calculo de la serie de Fibonacci
    if i == 0 :
        actual = 0
    elif i == 1:
        actual = 1
    else :
        actual = a + b
        a = b
        b = actual

    if actual % 2 == 0 : #determinamos si el término es par o impar (el cero es par)
        paridad  = "par"
        contador_pares += 1
    else : 
        paridad = "impar"
    print(f"El término {i+1} de la serie de Fibonacci es: {actual} y es {paridad}") #el programa analiza si es par o impar

proporcion = contador_pares / n if n > 0 else 0 #proporcion de pares sobre el total de terminos
print (f"La proporción de términos pares en la serie de Fibonacci es: {proporcion*100:.2f}%")
#el print final es para que el programa muestre en porcentaje la proporcion de pares sobre el total de terminos