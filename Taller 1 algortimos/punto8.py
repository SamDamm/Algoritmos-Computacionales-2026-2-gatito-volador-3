# Taller numero 1 Algoritmos
# Samuel Ricardo Cala Herrera 2251450
# Nicolas de Jesus Gonzalez Gamboa 2251867
# 1/09/2026
# Ejercicio 8

while True:
    lado_a = float(input("Introduce el cateto1 (0 para terminar): "))

    if lado_a == 0:
        print("Programa terminado.")
    break

lado_b = float(input("Introduce el cateto 2: "))
lado_c = float(input("Introduce el cateto 3: "))

if lado_a < 0 or lado_b <= 0 or lado_c <= 0:
        print("Error: las longitudes deben ser positivas.")

if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
    print("Los valores no pueden formar un triángulo.")

lados = sorted((lado_a, lado_b, lado_c))
lado_menor, lado_medio, lado_mayor = lados

if lado_menor == lado_mayor:
    tipo_lados = "equilátero"

elif lado_menor == lado_medio or lado_medio == lado_mayor:
    tipo_lados = "isósceles"

else:
    tipo_lados = "escaleno"

cuadrado_mayor = lado_mayor ** 2
suma_cuadrados = lado_menor ** 2 + lado_medio ** 2

if cuadrado_mayor == suma_cuadrados:
    tipo_angulos = "rectángulo"

elif cuadrado_mayor < suma_cuadrados:
    tipo_angulos = "acutángulo"

else:
    tipo_angulos = "obtusángulo"

print(f"Triángulo válido: {tipo_lados} y {tipo_angulos}.")
