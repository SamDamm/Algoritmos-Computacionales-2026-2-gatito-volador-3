#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 5

#Bienvenida del usuario al programa
print("-----------------------------------------------------")
print("REPARTO DE HERENCIA (SUMAS DE RIEMANN)")
print("-----------------------------------------------------")

def evaluar_polinomio(coefs, x): #Polinomio de grado n evaluado en x
  val = 0
  for c in coefs:
    val = val * x + c
  return val

def recortar(y):
  if y < 0: return 0
  elif y > 1: return 1
  return y

while True:
  grado_str = input("Ingrese el grado del polinomio (20 para salir): ")
  if grado_str.isdigit():
    grado = int(grado_str)
    if grado == 20:
      print("Fin del programa.")
      break
    
    coefs_input = input(f"Ingrese los {grado + 1} coeficientes separados por espacio: ")
    coefs = [int(c) for c in coefs_input.split()]
    
    n = int(input("Ingrese el número de rectángulos n: ")) #Sumatoria de Riemann de toda la vida
    
    ancho = 1.0 / n
    a_cain = 0.0
    for i in range(n):
      xi = i / n
      yi = evaluar_polinomio(coefs, xi)
      a_cain += ancho * recortar(yi)
      
    a_abel = 1.0 - a_cain
    dif = abs(a_cain - a_abel) #Determinar quien tiene más herencia o si es justo
    
    print(f"Área Caín: {a_cain:.4f} | Área Abel: {a_abel:.4f}")
    if dif <= 0.001:
      print("Resultado: JUSTO")
    elif a_cain > a_abel:
      print("Resultado: CAIN")
    else:
      print("Resultado: ABEL")
  else:
    print("Ingrese un valor válido.")