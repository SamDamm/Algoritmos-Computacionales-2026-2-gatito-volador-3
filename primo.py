n = int(input("Numero a probar: "))

divisores = 0
i = 2
while i < n:
    if n % i == 0:
        divisores += 1
    i += 1
if divisores > 0:
    print("No es primo") 
else :
    print("Es primo")
