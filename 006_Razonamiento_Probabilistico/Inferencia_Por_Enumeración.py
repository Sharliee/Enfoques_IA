# Definimos las probabilidades condicionales
P_D_si = 0.01
P_D_no = 0.99
P_S_si_D_si = 0.8
P_S_si_D_no = 0.1

# Enumeramos los posibles estados
estados = [(True, True), (True, False), (False, True), (False, False)]

# Calculamos la probabilidad conjunta de cada estado
P = {}
for d, s in estados:
    if d:
        P[(d, s)] = P_D_si * P_S_si_D_si if s else P_D_si * (1 - P_S_si_D_si)
    else:
        P[(d, s)] = P_D_no * P_S_si_D_no if s else P_D_no * (1 - P_S_si_D_no)

# Calculamos la probabilidad de que D sea Sí dado que S es Sí
P_D_si_S_si = sum([P[(d, s)] for d, s in estados if d and s]) / sum([P[(d, s)] for d, s in estados if s])

print("La probabilidad de que el paciente tenga la enfermedad dado que tiene síntomas es:", P_D_si_S_si)


