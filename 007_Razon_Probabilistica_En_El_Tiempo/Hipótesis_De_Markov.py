import numpy as np
import matplotlib.pyplot as plt

# Definimos la matriz de transición
P = np.array([[0.5, 0.5],
              [0.5, 0.5]])

# Definimos el estado inicial
estado_actual = 0  # Iniciamos en "cara"

# Generamos una lista de estados
estados = [estado_actual]
for i in range(99):
    # Generamos un número aleatorio entre 0 y 1
    r = np.random.rand()
    
    # Determinamos el siguiente estado
    if r < P[estado_actual][0]:
        estado_siguiente = 0  # Pasamos a "cara"
    else:
        estado_siguiente = 1  # Pasamos a "cruz"
    
    # Actualizamos el estado actual
    estado_actual = estado_siguiente
    estados.append(estado_actual)

# Graficamos los estados
plt.plot(estados)
plt.xlabel("Tiempo")
plt.ylabel("Estado")
plt.title("Proceso de lanzamiento de una moneda")
plt.show()
