salida = ""
palabra = input("ingrese su palabra: ")
letras = [x for x in palabra]
invert = letras.split(" ")
for i in range(len(invert)):
    salida = invert[i] + salida

print (salida)

