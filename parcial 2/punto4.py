#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 4

import matplotlib.pyplot as plt
import numpy as np

#Bienvenida del usuario al programa
print("-----------------------------------------------------")
print("PROYECCIÓN DE UN VECTOR SOBRE VECTORES UNITARIOS")
print("Instrucción: Ingrese componentes x y. Ingrese '0 0' para salir.")
print("-----------------------------------------------------")

np.random.seed(42)

while True:
  entrada = input("Ingrese un vector en coordenadas de (x y) o '0 0' para terminar: ")
  partes = entrada.split()
  if len(partes) != 2:
    print("Formato incorrecto. Ingrese dos números separados por espacio.") #Asegurar que el usuario ponga un vector válido
    continue
  x, y = float(partes[0]), float(partes[1])
  if x == 0 and y == 0:
    print("Programa finalizado.")
    break

#Calculo de las proyecciones de u sobre dos vectores unitarios aleatorios
  u = np.array([x, y])
  theta1, theta2 = np.random.uniform(0, 2 * np.pi, 2)
  v1 = np.array([np.cos(theta1), np.sin(theta1)])
  v2 = np.array([np.cos(theta2), np.sin(theta2)])

  p1 = (np.dot(u, v1)) * v1
  p2 = (np.dot(u, v2)) * v2

  print(f"Vector u: ({u[0]:.3f}, {u[1]:.3f})")
  print(f"Ángulo v1: {np.degrees(theta1):.3f}° | p1: ({p1[0]:.3f}, {p1[1]:.3f})")
  print(f"Ángulo v2: {np.degrees(theta2):.3f}° | p2: ({p2[0]:.3f}, {p2[1]:.3f})")

  #Graficas en matplotlib
  plt.figure(figsize=(5, 5))
  plt.quiver([0, 0, 0], [0, 0, 0], [u[0], p1[0], p2[0]], [u[1], p1[1], p2[1]],
             angles='xy', scale_units='xy', scale=1, color=['blue', 'green', 'orange'])
  lim = max(np.max(np.abs(u)), np.max(np.abs(p1)), np.max(np.abs(p2))) + 1
  plt.xlim(-lim, lim)
  plt.ylim(-lim, lim)
  plt.axhline(0, color='grey', lw=0.8)
  plt.axvline(0, color='grey', lw=0.8)
  plt.grid(True, ls='--')
  plt.title(f"Proyecciones de u = ({x}, {y})")
  plt.show()