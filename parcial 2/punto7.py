#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 7

# Tabla de conversión de mayor a menor
TABLA = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
    (1, "I"),
]

def a_romano(n):
    resultado = ""
    for valor, simbolo in TABLA:
        while n >= valor:
            resultado += simbolo
            n -= valor
    return resultado

while True:
    entrada = input("Numero: ")

    # Validar que sea un entero
    try:
        n = int(entrada)
    except ValueError:
        print("ERROR: debe ingresar un numero entero positivo")
        continue

    if n == 0:
        print("fin")
        break

    if n < 1 or n > 3999:
        print("ERROR: el numero debe estar entre 1 y 3999")
        continue

    print(a_romano(n))