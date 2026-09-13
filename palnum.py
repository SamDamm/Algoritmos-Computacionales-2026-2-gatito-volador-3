entrada = input("Que frase quiere contare?: ")
salida = " "
palabras = entrada.split(" ")
cantidad = len(palabras)
longitud = len(entrada)

for i in range(len(palabras)):
    #print(palabras[i])
    salida = palabras[i] + " " + salida

print(salida)
print(cantidad)
print(longitud)

for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {len(palabra)} letras")
