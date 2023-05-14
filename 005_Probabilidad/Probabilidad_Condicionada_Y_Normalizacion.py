# número de caras del dado
n_caras = 6

# número de resultados pares
n_pares = n_caras // 2

# número de resultados que son 6 y pares
n_6_y_pares = 1

# probabilidad de obtener un número par
prob_pares = n_pares / n_caras

# probabilidad de obtener un 6 y un número par
prob_6_y_pares = n_6_y_pares / n_caras

# probabilidad de obtener un 6, dado que el resultado es un número par
prob_6_cond_pares = prob_6_y_pares / prob_pares

print("La probabilidad de obtener un 6, dado que el resultado es un número par, es:", prob_6_cond_pares)

# lista de probabilidades
probs = [0.2, 0.3, 0.1, 0.4]

# suma de las probabilidades
sum_probs = sum(probs)

# normalización de las probabilidades
norm_probs = [p / sum_probs for p in probs]

print("Lista de probabilidades original:", probs)
print("Lista de probabilidades normalizada:", norm_probs)