# Importar módulo de SOM
from minisom import MiniSom #Se importa la librería MiniSom.
import numpy as np #Se importa la librería NumPy.

# Definir la matriz de datos
datos = np.array([[1.2, 2.3], [2.1, 1.7], [1.9, 1.4], [1.5, 2.0]])
#Se define la matriz de datos como un arreglo NumPy de 4 filas y 2 columnas, con valores flotantes.

# Definir el tamaño del mapa auto-organizado
tamanio_mapa = (2, 2)

# Crear el mapa auto-organizado y entrenarlo
modelo = MiniSom(tamanio_mapa[0], tamanio_mapa[1], datos.shape[1])
#Se define el tamaño del mapa auto-organizado como una tupla de 2x2.
#Se crea una instancia de la clase MiniSom, con el tamaño del mapa y el número de características de los datos.

modelo.train_random(datos, 100)

# Mostrar el mapa auto-organizado y las neuronas ganadoras para cada dato
#Se entrena el modelo con los datos utilizando el método "train_random", que es un método de entrenamiento que utiliza el algoritmo de Kohonen.
#Se muestra el mapa auto-organizado y las neuronas ganadoras para cada dato en un bucle "for". El método "winner" devuelve la neurona ganadora para
#cada dato, y el método "get_weights" devuelve los pesos de las neuronas del mapa.

for i, x in enumerate(datos):
    ganador = modelo.winner(x)
    print("Dato:", x, "- Neurona ganadora:", ganador)
    print("Mapa auto-organizado:")
    print(modelo.get_weights())
