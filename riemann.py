import math

a = float(input("Por fa el a: "))
b = float(input("Introduzca el b: "))
n = int(input("Cuantos pasos? (n): "))
dx = (b - a) / n
suma = 0
for i in range(n):
    x = a + i * dx
    y = math.sin(x) ** 2 + x
    suma = suma + y * dx
print(f"El valor aproximado de la integral es: {suma}")