def generar_numeros():
    historial = leer_historial()

    # Si no hay historial → random inicial
    if not historial:
        combinacion = sorted(random.sample(range(1, 57), 6))
        guardar_historial(combinacion)
        return combinacion

    frecuencia = analizar_frecuencia(historial)

    # ordenar números más frecuentes
    ordenados = sorted(frecuencia, key=frecuencia.get, reverse=True)

    # top inteligentes + mezcla aleatoria
    top = ordenados[:20] if ordenados else list(range(1,57))

    combinacion = sorted(random.sample(top, 6))

    # guardar para aprendizaje
    guardar_historial(combinacion)

    return combinacion
    with open(DATA_FILE, "w") as f:
        json.dump(historial, f)
