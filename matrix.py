import numpy as np
from time import perf_counter_ns

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

inicio = perf_counter_ns()
resultado = np.dot(A, B)
fin = perf_counter_ns()

print("Matriz A:")
print(A)
print("Matriz B:")
print(B)
print("Resultado A x B:")
print(resultado)

tiempo_ns = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ns} ns")
print(f"Tiempo de ejecución: {tiempo_ns / 1000:.3f} µs")
print(f"Tiempo de ejecución: {tiempo_ns / 1_000_000:.6f} ms")