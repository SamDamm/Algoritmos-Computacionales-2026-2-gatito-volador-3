#Ejercicio 1 
#Samuel Cala 2251450

opcion = int(input("Ingrese un numero positivo entero: "))
temp = opcion 
binario = "" 

if temp == 0: #cuando el binario es 0
    binario = "0"
else : #hallar el binario diviendo entre dos y sumando el termino binario
    while temp > 0:
        residuo = temp % 2
        binario = str(residuo) + binario #uso el string para concatenar el residuo al binario
        temp = temp // 2

print(f"El numero binario es: {binario}")
