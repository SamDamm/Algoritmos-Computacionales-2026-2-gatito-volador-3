numero = int(input("Ingrese un numero para calcular su factorial: "))

fact = 1
i = 1

while i <= numero :
    fact = fact * i
    i = i + 1

print(fact)