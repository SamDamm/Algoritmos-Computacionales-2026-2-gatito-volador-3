num_terminos = int(input("Ingrese el número de términos de la serie de Fibonacci: "))

penultimo = 0
ultimo = 1

for i in range(num_terminos):
    if i <= 1:
        siguiente = i
    else:
        siguiente = penultimo + ultimo
        penultimo = ultimo
        ultimo = siguiente
    print(siguiente, end=" ")
