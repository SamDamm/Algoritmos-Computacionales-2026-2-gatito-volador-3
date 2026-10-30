#Parcial #2 Algoritmos
#Samuel Ricardo Cala Herrera 2251450
#Nicolas de Jesus Gonzalez Gamboa 2251867
#29/10/2026
#Ejercicio 9

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def lorenz_derivadas(t, estado, sigma, rho, beta):
    """empezamos definiendo dx/dt, dy/dt, dz/dt dados por las ecuaciones de lorenz.
    Puede recibir un solo punto o sea un array 1D o varios puntos a la vez array 2D.
    """
    
    #si estado es 2D se desempaqueta por columnas, de lo contrario solo mantenemos un estado 
    if estado.ndim == 2:
        x, y, z = estado[:, 0], estado[:, 1], estado[:, 2]
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return np.column_stack((dx_dt, dy_dt, dz_dt))
    else: 
        x, y, z = estado
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return np.array([dx_dt, dy_dt, dz_dt])

def runge_kutta_4_paso(f, t, y, h, *args):
    #acá metemos la funcion del metodo de runge kutta, sirve para aproximar la pendiente en diferentes puntos sobre un intervalo de tiempo h y luego promedia esas pendientes para obtener una mejor aproximación del valor siguiente.
    k1 = h * f(t, y, *args)
    k2 = h * f(t + 0.5*h, y + 0.5*k1, *args)
    k3 = h * f(t + 0.5*h, y + 0.5*k2, *args)
    k4 = h * f(t + h, y + k3, *args)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0


#se crea la funcion para integrar por bucles y calcular el tiempo que dura esta forma
def integrar_bucle(puntos_iniciales, t_values, h, sigma, rho, beta):
    n_puntos = len(puntos_iniciales)
    n_pasos = len(t_values)
    trayectorias = np.zeros((n_puntos, n_pasos, 3))
    
    start_time = time.time()
    for i in range(n_puntos):
        estado_actual = puntos_iniciales[i].copy()
        trayectorias[i, 0] = estado_actual
        for j in range(1, n_pasos):
            estado_actual = runge_kutta_4_paso(
                lorenz_derivadas, t_values[j-1], estado_actual, h, sigma, rho, beta
            )
            trayectorias[i, j] = estado_actual
            
    tiempo_total = time.time() - start_time
    return trayectorias, tiempo_total


#acá se hacen las integraciones pero usando numpy nuevamente se busca mirar la eficiencia de hacer la integracion así
def integrar_vectorizado(puntos_iniciales, t_values, h, sigma, rho, beta):
    n_puntos = len(puntos_iniciales)
    n_pasos = len(t_values)
    trayectorias = np.zeros((n_pasos, n_puntos, 3))
    
    start_time = time.time()
    estado_actual = np.array(puntos_iniciales)
    trayectorias[0] = estado_actual
    
    for j in range(1, n_pasos):
        estado_actual = runge_kutta_4_paso(
            lorenz_derivadas, t_values[j-1], estado_actual, h, sigma, rho, beta
        )
        trayectorias[j] = estado_actual
        
    tiempo_total = time.time() - start_time
    return np.transpose(trayectorias, (1, 0, 2)), tiempo_total


#funcion para las graficas del modelo
def graficar_trayectorias(trayectorias, titulo):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    n_puntos = trayectorias.shape[0]
    for i in range(n_puntos):
        x = trayectorias[i, :, 0]
        y = trayectorias[i, :, 1]
        z = trayectorias[i, :, 2]
        ax.plot(x, y, z, lw=0.5, alpha=0.8, label=f'Trayectoria {i+1}')
        
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title(titulo)
    plt.tight_layout()
    plt.show()
