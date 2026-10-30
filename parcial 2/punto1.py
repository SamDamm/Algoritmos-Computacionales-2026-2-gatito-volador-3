#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 1

#Bienvenida al programa para el usuario
print("-----------------------------------------------------")
print("CIFRADO Y DESCIFRADO DE CÉSAR CON SALTO POR POSICIÓN")
print("-----------------------------------------------------")

modo = input("Ingrese el modo ('C' para cifrar, 'D' para descifrar): ").strip().upper()
frase = input("Ingrese la frase a procesar: ") #Indicaciones que debe cumplir el usuario para que el programa funcione

palabras = frase.split(" ")
resultado_palabras = []

for idx, palabra in enumerate(palabras):
  k = 3 if idx % 2 == 0 else 4 #Con k determinamos el salto según la posición, 3 para pares y 4 para impares
  palabra_mod = ""

  for char in palabra:
    if "a" <= char <= "z":
      base = ord("a")
      pos = ord(char) - base
      if modo == "C":
        nueva_pos = (pos + k) % 26
      elif modo == "D":
        nueva_pos = (pos - k) % 26
      else:
        nueva_pos = pos  #Para que no haya ningún cambio si el modo no es válido
      palabra_mod += chr(base + nueva_pos)

    elif "A" <= char <= "Z":
      base = ord("A")
      pos = ord(char) - base
      if modo == "C":
        nueva_pos = (pos + k) % 26
      elif modo == "D":
        nueva_pos = (pos - k) % 26
      else:
        nueva_pos = pos
      palabra_mod += chr(base + nueva_pos)
    else:
      #Todo lo que no sea una letra, excepto ñ, se mantiene igual
      palabra_mod += char

  resultado_palabras.append(palabra_mod)

frase_procesada = " ".join(resultado_palabras)
print("[Resultado]")
print("Frase procesada:", frase_procesada)