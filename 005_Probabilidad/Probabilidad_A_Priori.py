import numpy as np

# Generamos una lista de 100 números aleatorios del 1 al 10
numeros = np.random.randint(1, 11, 100)

# Suponemos que la probabilidad a priori de que un número sea mayor que 5 es 0.4
prob_priori_mayor_5 = 0.4

# Calculamos la probabilidad a posteriori de que un número sea mayor que 5
prob_mayor_5 = sum(numeros > 5) / len(numeros)
prob_posteriori_mayor_5 = (prob_mayor_5 * prob_priori_mayor_5) / ((prob_mayor_5 * prob_priori_mayor_5) + ((1 - prob_mayor_5) * (1 - prob_priori_mayor_5)))

print("La probabilidad a priori de que un número sea mayor que 5 es:", prob_priori_mayor_5)
print("La probabilidad a posteriori de que un número sea mayor que 5 es:", prob_posteriori_mayor_5)
