import numpy as np
from hmmlearn import hmm

# Importar las librerías necesarias para trabajar con modelos HMM

# Definir el modelo oculto de Markov
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Crear un objeto de modelo HMM con 2 estados y una distribución gaussiana para las observaciones

# Definir los parámetros del modelo
model.startprob_ = np.array([0.6, 0.4]) # Probabilidad inicial
model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]]) # Matriz de transición
model.means_ = np.array([[0.0], [3.0]]) # Media
model.covars_ = np.array([[1.0], [1.5]]) # Varianza

# Definir los parámetros del modelo, como la probabilidad inicial, la matriz de transición, la media y la varianza de la distribución gaussiana de las observaciones

# Definir la secuencia de observaciones
obs = np.array([[0.5], [2.0], [-0.3], [4.1]])

# Crear una matriz numpy de 4x1 con los valores de la secuencia de observaciones

# Calcular las probabilidades hacia adelante
logprob, fwdlattice = model.score_samples(obs)
fwdlattice = np.exp(fwdlattice)

# Calcular la log-probabilidad de la secuencia de observaciones y las probabilidades hacia adelante utilizando el método score_samples del modelo. Luego, convertir las probabilidades hacia adelante de logaritmos a valores reales

# Calcular las probabilidades hacia atrás
bwdlattice = model.decode(obs)[0]

# Calcular las probabilidades hacia atrás utilizando el método decode del modelo y seleccionando la primera salida del resultado

# Calcular la distribución posterior
posterior = fwdlattice * bwdlattice / np.sum(fwdlattice * bwdlattice, axis=1, keepdims=True)

# Calcular la distribución posterior combinando las probabilidades hacia adelante y hacia atrás. Primero, multiplicar las probabilidades hacia adelante y hacia atrás para obtener la distribución conjunta. Luego, normalizar esta distribución conjunta para obtener la distribución posterior

print("La distribución posterior es:")
print(posterior)
