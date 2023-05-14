#Busqueda local de minimos conflictos
import random

def busqueda_local_min_conflictos(problema, max_iter=1000, max_pasos=100):

    # Generar estado inicial aleatorio
    estado_actual = problema.estado_aleatorio()

    for i in range(max_iter):
        # Comprobar si el estado actual es objetivo
        if problema.es_estado_objetivo(estado_actual):
            return ([estado_actual], True)

        # Realizar búsqueda local de mínimos conflictos
        for j in range(max_pasos):
            # Obtener la lista de variables conflictivas en el estado actual
            var_conflictivas = problema.variables_conflictivas(estado_actual)

            # Comprobar si no hay variables conflictivas
            if not var_conflictivas:
                break

            # Escoger una variable conflictiva aleatoria
            var = random.choice(var_conflictivas)

            # Escoger un valor para la variable conflictiva que minimice los conflictos
            val = problema.valor_min_conflictos(var, estado_actual)

            # Asignar el valor a la variable
            estado_actual[var] = val

    # Si no se encontró solución, retornar False y una lista vacía
    return (False, [])
