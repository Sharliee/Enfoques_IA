# Importar módulo de HMM
from hmmlearn import hmm

# Definir el modelo oculto de Markov
modelo = hmm.GaussianHMM(n_components=2)
#En esta línea se crea un objeto GaussianHMM que
#representa el modelo oculto de Markov. GaussianHMM 
#es una clase proporcionada por la librería hmmlearn
#que implementa un modelo oculto de Markov con emisiones 
#gaussianas continuas. En este caso, se está creando un modelo
#con dos estados ocultos.

# Entrenar el modelo con una secuencia de observaciones
secuencia = [[1.5], [2.0], [1.7], [2.3], [1.9]]
modelo.fit(secuencia)
#se entrena el modelo oculto de Markov utilizando la secuencia
#de observaciones secuencia. El modelo aprende los parámetros
#para generar las observaciones a partir de los estados latentes
#del modelo.

# Generar una secuencia de observaciones a partir del modelo
secuencia_generada, estados = modelo.sample(n_samples=5) 
#utiliza el modelo entrenado para generar una nueva secuencia 
#de 5 observaciones y devuelve tanto la secuencia como los 
#estados del modelo.

# Mostrar la secuencia generada y los estados del modelo
print("Secuencia generada:", secuencia_generada)
print("Estados del modelo:", estados)
