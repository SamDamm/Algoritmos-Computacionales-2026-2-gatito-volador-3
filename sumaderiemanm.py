def suma_riemann(f, a, b, n, metodo='izquierda'):
    dx = (b - a) / n
    suma = 0.0
    
    for i in range(n):
        if metodo == 'izquierda':
            x = a + i * dx
        elif metodo == 'derecha':
            x = a + (i + 1) * dx
        elif metodo == 'medio':
            x = a + (i + 0.5) * dx
        else:
            raise ValueError("Método no válido. Usa 'izquierda', 'derecha' o 'medio'.")
        
        suma += f(x)
    
    return suma * dx

# Ejemplo de uso: f(x) = x^2 en el intervalo [0, 2] con n = 1000 subintervalos
funcion = lambda x: x**2
a, b = 0, 2
n = 1000

print(f"Suma por la izquierda: {suma_riemann(funcion, a, b, n, 'izquierda'):.6f}")
print(f"Suma por el punto medio: {suma_riemann(funcion, a, b, n, 'medio'):.6f}")
print(f"Suma por la derecha:   {suma_riemann(funcion, a, b, n, 'derecha'):.6f}")