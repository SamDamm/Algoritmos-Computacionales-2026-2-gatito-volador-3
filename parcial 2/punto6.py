#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 6

import numpy as np

while True:
    # Validar el tamaño n
    texto_n = input("Tamaño de la matriz (0 para terminar): ")
    try:
        n = int(texto_n)
    except ValueError:
        print("ERROR: debe ingresar un numero entero")
        continue

    if n == 0:
        break

    if n < 0 or n > 50:
        print("ERROR: el tamaño debe estar entre 1 y 50")
        continue

    # Pedir las filas
    filas = []
    while len(filas) < n:
        texto = input("Fila " + str(len(filas) + 1) + ": ")

        # Aceptar "1 2 3", "1,2,3" o "[1, 2, 3]"
        texto = texto.replace(",", " ").replace("[", " ").replace("]", " ")
        partes = texto.split()

        # Validar que cada elemento sea un entero
        try:
            fila = [int(x) for x in partes]
        except ValueError:
            print("ERROR: solo se permiten numeros enteros (sin letras ni decimales)")
            continue

        # Validar que la fila tenga n elementos
        if len(fila) != n:
            print("ERROR: la fila debe tener", n, "numeros separados por espacios")
            continue

        filas.append(fila)

    matriz = np.array(filas)

    print("Matriz:")
    print(matriz)
    print("Forma:", matriz.shape)

    arriba = np.triu(matriz, 1)
    abajo = np.tril(matriz, -1)

    if np.any(arriba != 0) and np.any(abajo != 0):
        print("NO")
    else:
        print("SI")