#Taller numero 1 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#1/09/2026
#Ejercicio 1
import math as mt
while True:
    opcion = 0
    print("-------------------------------------------")
    print("CALCULADORA DE FUNCIONES")
    print("-------------------------------------------")
    print("Si desea calcular el seno escriba 1")
    print("si lo que quiere es calcular el coseno escriba 2")
    print("y si quiere calcular la tangente escriba 3")
    print("Si ya termino marque 4")
    print("-------------------------------------------")

    opcion = int(input("Tenga la amabilidad de seleccionar una opcion: "))

    if opcion == 1:

        ntermino = int(input("Sea tan amable de ingresa el numero de terminos: "))
        angulo = int(input("Sea tan amable de ingresar el angulo: "))
        x = (3.14159265358979 * angulo) / 180
        suma = 0

        for i in range(ntermino):

            fact = 1
            j = 1
            lim = 2 * i + 1
            while j <= lim:
                fact = fact * j
                j = j + 1
                
            termino = ((-1)**i) * (x**(2*i+1)) / fact
            suma = suma + termino

        print(f"El resultado del seno con angulo {angulo} es {suma}")

    elif opcion == 2:
        ntermino = int(input("Sea tan amable de ingresa el numero de terminos: "))
        angulo = int(input("Sea tan amable de ingresar el angulo: "))
        x = (3.14159265358979 * angulo) / 180
        suma = 0
        
        for i in range(ntermino):
        
                fact = 1
                j = 1
                lim = 2 * i 
                while j <= lim:
                    fact = fact * j
                    j = j + 1
                    
                termino = ((-1)**i) * (x**(2*i)) / fact
                suma = suma + termino
        
        print(f"El resultado del coseno con angulo {angulo} es {suma}")

    elif opcion == 3:
        print("esto todavia no se puede, intentelo mas tarde")
    elif opcion == 4:
        print(
            "Fin"
        )

    else:
        print("vuelva a intentarlo y seleccione un campo valido, del 1 al 4")
    break