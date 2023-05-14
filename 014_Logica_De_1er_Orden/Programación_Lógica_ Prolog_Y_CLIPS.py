# Definimos algunos hechos
tiene_pelo = ["gato", "perro", "vaca"]
da_leche = ["vaca", "cabra"]

# Definimos la regla para determinar si un animal es mamífero
def es_mamifero(animal):
    if animal in tiene_pelo or animal in da_leche:
        return True
    else:
        return False

# Ejemplos de consultas
print(es_mamifero("gato"))  # True
print(es_mamifero("pato"))  # False

# Solicitamos los datos del usuario
nombre = input("Nombre: ")
promedio = float(input("Promedio: "))
materias_reprobadas = int(input("Materias reprobadas: "))
ingresos = float(input("Ingresos mensuales: "))

# Evaluamos las reglas
if promedio >= 90 and materias_reprobadas == 0 and ingresos <= 15000:
    print(f"{nombre} es elegible para la beca.")
else:
    print(f"{nombre} no es elegible para la beca.")
