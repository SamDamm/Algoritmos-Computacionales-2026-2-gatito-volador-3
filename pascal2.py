import math as m


filas = int(input("Cuantas filas quiere calcular: "))

i = 0
while i <= filas :
    j = 0
    while j < i :
        print(f"({i},{j})", end = " ")
        n = i
        r = j
        factn = 1
        while n > 0 :
            factn = factn * n
            n = n - 1
        factr = 1
        while r > 0 :
            factr = factr * r
            r = r - 1

        nr = i - j
        factnr = 1
        while nr > 0 :
            factnr = factnr * nr
            nr = nr - 1

        # calculo del numero
        ncomb = factn / (factr * factnr)
        print(f"({i},{j}) = {int(ncomb)}", end = " ")

        j = j + 1
        print("")
    i = i + 1