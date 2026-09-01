entrada = input("Que quiere invertir?: ")
salida = ""

for i in range(len(entrada)):
    print(entrada[i])
    salida = entrada[i] + salida

if salida == entrada:
    print("Es un palindromo")
else:
    print("No es un palindromo")

print(salida)