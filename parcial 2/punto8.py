#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 8

def pares_objetivo(lista, objetivo):
    vistos = set()
    pares = set()
    
    for num in lista:
        complemento = objetivo - num
        
       
        if complemento in vistos:
            # Aseguramos el formato a <= b
            a = min(num, complemento)
            b = max(num, complemento)
            pares.add((a, b)) # El set evita que se repitan los pares
        
        # Guardamos el número actual para futuras comparaciones
        vistos.add(num)
        
    # Ordenamos la lista de pares (por defecto ordena por 'a' y luego por 'b')
    for a, b in sorted(pares):
        print(f"{a}, {b}")
