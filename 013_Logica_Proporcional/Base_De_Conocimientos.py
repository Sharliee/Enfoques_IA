temperatura = 32
humedad = 85

if temperatura > 30:
    hace_calor = True
else:
    hace_calor = False

if humedad > 80:
    posibilidad_lluvia = True
else:
    posibilidad_lluvia = False

if hace_calor and posibilidad_lluvia:
    hay_tormenta = True
else:
    hay_tormenta = False

print("¿Hay tormenta?", hay_tormenta)