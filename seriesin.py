angulo = int(input("Ingrese el angulo en grados: "))
x = (3.1416 * angulo) / 180
suma = 0

ntermino = int(input("Ingrese el numero de terminos: "))
for i in range(ntermino):
    fact = 1
    j = 1
    lim = 2 * i + 1
    while j <= lim:
        fact = fact * j
        j = j + 1
    suma = suma + ((-1)**i) * (x**lim) / fact
print(f"El valor aproximado del seno es: {suma}")
