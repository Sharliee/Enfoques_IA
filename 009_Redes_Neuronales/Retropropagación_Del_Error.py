from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import numpy as np

# Generamos datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # entradas
y = np.array([0, 1, 1, 0]) # salidas deseadas

# Definimos la arquitectura de la red neuronal
model = Sequential() # modelo secuencial
model.add(Dense(2, input_dim=2, activation='sigmoid')) # capa densa con 2 neuronas y función de activación sigmoidal
model.add(Dense(1, activation='sigmoid')) # capa de salida con 1 neurona y función de activación sigmoidal

# Compilamos el modelo
sgd = SGD(lr=0.1) # optimizador SGD con tasa de aprendizaje 0.1
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy']) # compilamos el modelo con función de pérdida de entropía cruzada binaria y métrica de precisión

# Entrenamos el modelo
model.fit(X, y, epochs=1000, verbose=0) # entrenamos el modelo con los datos de entrada X y las salidas deseadas y durante 1000 épocas

# Evaluamos el modelo entrenado
scores = model.evaluate(X, y) # evaluamos el modelo en los mismos datos de entrada y salidas deseadas para ver la precisión
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) # mostramos la precisión del modelo
