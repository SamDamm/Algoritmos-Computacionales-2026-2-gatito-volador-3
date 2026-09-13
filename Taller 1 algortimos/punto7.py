# Taller numero 1 Algoritmos
# Samuel Ricardo Cala Herrera 2251450
# Nicolas de Jesus Gonzalez Gamboa 2251867
# 1/09/2026
# Ejercicio 7

datos = []
num_valido = False
while not num_valido:
  entrada = input("Numero elementos: ")
  if entrada.isdigit():
    num = int(entrada)
    if num > 0:
      num_valido = True
    else:
      print("El número de elementos debe ser mayor a 0.")
  else:
    print("Debe ingresar un número entero positivo.")

for i in range(num):
  elemento_valido = False
  while not elemento_valido:
    entrada_elem = input(f"Elemento {i+1}?: ")
    es_entero = True
    if entrada_elem == "":
      es_entero = False
    else:
      inicio = 0
      if entrada_elem[0] == "-":
        if len(entrada_elem) == 1:
          es_entero = False
        else:
          inicio = 1
      for j in range(inicio, len(entrada_elem)):
        c = entrada_elem[j]
        if c < "0" or c > "9":
          es_entero = False

    if es_entero:
      datos.append(int(entrada_elem))
      elemento_valido = True
    else:
      print("Debe ser un número entero. Intente de nuevo.")

print("Lista de datos ingresados:", datos)

unicos = []
frecuencias = []

for x in datos:
  encontrado = False
  for k in range(len(unicos)):
    if unicos[k] == x:
      frecuencias[k] += 1
      encontrado = True
      break
  if not encontrado:
    unicos.append(x)
    frecuencias.append(1)

max_freq = 0
for f in frecuencias:
  if f > max_freq:
    max_freq = f

if max_freq == 1:
  print("Resultado: Ningún valor se repite en el conjunto. Por lo tanto, el" " conjunto NO TIENE MODA.")
else:
  modas = []
  for k in range(len(frecuencias)):
    if frecuencias[k] == max_freq:
      modas.append(unicos[k])

  if len(modas) > 1:
    print("El conjunto es MULTIMODAL, ya que hay varios valores que comparten" f" la misma frecuencia máxima ({max_freq} veces):")
    print("Las modas son:", modas)
  else:
   
    print("La moda es:", modas[0], f"con una frecuencia máxima de {max_freq} repeticiones.",)