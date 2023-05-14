#Importar módulo de incertidumbre
import numpy as np

# Definir un arreglo de probabilidades
probabilidades = np.array([0.2, 0.5, 0.3])

# Calcular la entropía de Shannon
#se define la función entropia_shannon, que calcula 
#la entropía de Shannon de un arreglo de probabilidades.
#Esta función toma un arreglo de probabilidades como entrada 
#y devuelve un valor numérico que representa la entropía.
def entropia_shannon(p):
    entropia = 0
    for i in range(len(p)):
        if p[i] > 0:
            entropia -= p[i] * np.log2(p[i])
    return entropia

# Calcular la entropía de Shannon del arreglo de probabilidades
entropia = entropia_shannon(probabilidades)
print("La entropía de Shannon es:", entropia)
