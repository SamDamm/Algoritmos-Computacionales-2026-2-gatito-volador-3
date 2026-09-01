def obtener_cuadrados(limite):
    return [k**2 for k in range(int(limite**0.5) + 1)]

# Entrada interactiva del usuario
limite_usuario = int(input("Ingresa el número límite: "))
resultado = obtener_cuadrados(limite_usuario)

print(f"Cuadrados perfectos hasta {limite_usuario}: {resultado}")