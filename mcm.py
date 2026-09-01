valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))   


mcm = valor1 * valor2  # Calculate LCM using GCD
if valor1 == valor2:
    print(f"El mcm es {valor2}")
elif valor1 > valor2 :
    for i in range(valor1*valor2, valor1 - 1, -1):
        if valor1 % i == 0 and valor2 % i == 0 :
            mcm = i
    print(f"El mcm es {mcm}")
else:
    for i in range(valor1*valor2, valor2 - 1, -1):
        if valor1 % i == 0 and valor2 % i == 0 :
            mcm = i
    print(f"El mcm es {mcm}")
