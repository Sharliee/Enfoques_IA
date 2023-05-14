import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter

# Intervalo de tiempo entre las mediciones
dt = 1.0

# Creamos un objeto KalmanFilter con 2 variables de estado y 1 variable de medida
kf = KalmanFilter(dim_x=2, dim_z=1)

# Matriz de transición de estado
kf.F = np.array([[1, dt], [0, 1]])

# Matriz de observación
kf.H = np.array([[1, 0]])

# Matriz de covarianza del proceso
kf.Q = np.array([[0.01, 0.], [0., 0.01]])

# Matriz de covarianza de la medida
kf.R = np.array([[0.1]])

# Inicializamos el filtro con un estado inicial y una matriz de covarianza inicial
kf.x = np.array([0., 0.]) # Estado inicial
kf.P = np.array([[1, 0], [0, 1]]) # Matriz de covarianza inicial

# Simulamos la posición del objeto con ruido aleatorio discreto

true_positions = [0]
measurements = [0]
for i in range(1, 100):
    # La posición del objeto se incrementa en 1 unidad por cada iteración
    true_positions.append(true_positions[i-1] + 1)
    # La medida es igual a la posición real más un ruido aleatorio entre -1 y 1
    measurements.append(true_positions[i] + np.random.randint(-1, 2))

# Aplicamos el filtro de Kalman para estimar la posición del objeto
estimated_positions = []
for z in measurements:
    # Predicción del estado y de la matriz de covarianza del filtro
    kf.predict()
    # Actualización del estado y de la matriz de covarianza del filtro con la medida
    kf.update(z)
    # Agregamos la posición estimada a la lista de posiciones estimadas
    estimated_positions.append(kf.x[0])

# Graficamos los resultados
plt.figure()
plt.plot(range(len(true_positions)), true_positions, label='Posición real')
plt.plot(range(len(measurements)), measurements, label='Posición medida')
plt.plot(range(len(estimated_positions)), estimated_positions, label='Posición estimada')
plt.legend()
plt.show()
