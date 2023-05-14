import numpy as np
import matplotlib.pyplot as plt

print("\n\n codigo de hamming \n\n")

def hamming_distance(s1, s2):
    """
    Calcula la distancia de Hamming entre dos cadenas de igual longitud.
    """
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# Ejemplo de uso
cadena1 = '01010101'
cadena2 = '01100110'
distancia = hamming_distance(cadena1, cadena2)
print(f"La distancia de Hamming entre {cadena1} y {cadena2} es {distancia}")

print("\n\n red de hopfield\n\n")

# Función de activación
def activation(x):
    return np.sign(x)

# Patrones de imagen
patterns = np.array([
    [-1, 1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1],
    
    [1, 1, 1, 1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     1, 1, 1, 1],
    
    [-1, 1, 1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, 1, 1, -1],
    
    [1, 1, 1, 1,
     1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1]
])

# Imágenes distorsionadas
distorted_patterns = np.array([
    [-1, 1, -1, 1,
     1, 1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1],
    
    [1, 1, 1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, 1],
    
    [-1, 1, 1, -1,
     1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, 1, -1, -1],
    
    [1, -1, -1, -1,
     1, -1, -1, 1,
     -1, -1, -1, -1,
     -1, -1, -1, 1]
])

# Inicializar matriz de pesos
W = np.zeros((patterns.shape[1], patterns.shape[1]))

# Entrenamiento
for pattern in patterns:
    pattern = pattern.reshape(-1, 1) # Convertir el patrón en un vector columna
    W += np.dot(pattern, pattern.T) # Actualizar la matriz de pesos

# Diagonal con ceros
np.fill_diagonal(W, 0) # La diagonal de la matriz de pesos se pone en 0

# Corrección de patrones distorsionados
for distorted_pattern in distorted_patterns:
    distorted_pattern = distorted_pattern.reshape(-1, 1) # Convertir la imagen distorsionada en un vector columna
    output = distorted_pattern.copy() # Inicializar la salida con la imagen distorsionada
    prev_output = np.zeros(output.shape) # Inicializar la salida previa
    counter = 0 # Contador de iteraciones
    while not np.array_equal(output, prev_output) and counter < 100:
        prev_output = output.copy() # Actualizar la salida previa
        for i in range(output.shape[0]):
            output[i] = activation(np.dot(W[i, :], output)) # Aplicar la regla de actualización a cada neurona
        counter += 1 # Incrementar el contador de iteraciones
    
    # Mostrar imágenes
    plt.figure()
    plt.subplot(121)
    plt.imshow(distorted_pattern.reshape(4, 4), cmap='gray')
    plt.title('Imagen Distorcionada')
    plt.subplot(122)
    plt.title('Imagen corregida')
    plt.imshow(output.reshape(4, 4), cmap='gray')
    
    
    
    
######################## regla de hebb

print("\n\n regla de hebb\n\n")

# Definir patrones de entrenamiento
patterns = np.array([
    [1, 1, 1, -1],      # Patrón 1
    [-1, -1, 1, 1],     # Patrón 2
    [1, -1, -1, -1],    # Patrón 3
    [-1, 1, -1, 1]      # Patrón 4
])

# Inicializar matriz de pesos con ceros
W = np.zeros((patterns.shape[1], patterns.shape[1]))

# Entrenamiento utilizando la regla de Hebb
for pattern in patterns:
    pattern = pattern.reshape(-1, 1)         # Cambia el patrón a una matriz columna
    W += np.dot(pattern, pattern.T)         # Actualiza la matriz de pesos utilizando la regla de Hebb

# Diagonal con ceros
np.fill_diagonal(W, 0)                      # Los pesos de una neurona consigo misma siempre son cero

# Función de activación
def activation(x):
    return np.where(x >= 0, 1, -1)           # Función escalón bipolar

# Prueba con patrones de entrenamiento
for pattern in patterns:
    pattern = pattern.reshape(-1, 1)         # Cambia el patrón a una matriz columna
    output = activation(np.dot(W, pattern)) # Calcula la salida utilizando la función de activación
    # Imprime el patrón de entrada y su correspondiente salida
    print(f'Entrada: {pattern.T}, Salida: {output.T}')

###########################   maquina de boltzman

print("\n\n maquina de boltzman\n\n")
