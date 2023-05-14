import numpy as np
import matplotlib.pyplot as plt

# Definimos los límites del espacio de configuración de cada articulación
limits = [(-np.pi/2, np.pi/2), (-np.pi/2, np.pi/2)]

# Generamos una lista con todas las posibles combinaciones de ángulos de articulación
angles = np.meshgrid(*[np.linspace(l[0], l[1], 50) for l in limits])
angles = np.vstack(list(map(np.ravel, angles))).T

# Calculamos las posiciones de cada articulación en función de los ángulos
x1 = np.cos(angles[:,0])
y1 = np.sin(angles[:,0])
x2 = x1 + np.cos(angles[:,0]+angles[:,1])
y2 = y1 + np.sin(angles[:,0]+angles[:,1])

# Graficamos el rango de movimiento del robot
plt.plot(x1, y1, 'b.', markersize=1)
plt.plot(x2, y2, 'r.', markersize=1)
plt.axis('equal')
plt.show()
