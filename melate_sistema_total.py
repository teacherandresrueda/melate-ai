import random
import json
import os

DATA_FILE = "historial_melate.json"

def leer_historial():
    if not os.path.exists(DATA_FILE):
        return []  # evita que falle

    with open(DATA_FILE, "r") as f:
        return json.load(f)
def generar_numeros():
    base = list(range(1, 57))
    
    # simular patrón (evitar repetidos recientes)
    seleccion = random.sample(base, 6)
    
    # ordenar (se ve más profesional)
    seleccion.sort()
    
    return seleccion

def analizar_frecuencia(numeros):
    frecuencia = {}
    for n in numeros:
        frecuencia[n] = frecuencia.get(n, 0) + 1
    return frecuencia

def generar_numeros():
    historial = leer_historial()
    frecuencia = analizar_frecuencia(historial)

    # ordenar por frecuencia (más repetidos)
    ordenados = sorted(frecuencia, key=frecuencia.get, reverse=True)

    # tomar top + random para balance
    top = ordenados[:15] if ordenados else list(range(1,57))

    combinacion = sorted(random.sample(top, 6))
    return combinacion
