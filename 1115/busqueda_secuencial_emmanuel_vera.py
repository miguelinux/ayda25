def busqueda_secuencial(aguja, pajar):
    # Recorremos el pajar desde el índice 0 hasta el final
    for indice in range(len(pajar)):
        if pajar[indice] == aguja:
            return indice

    # Si terminamos todo el recorrido y no regresamos índice,
    # significa que la aguja no está en el pajar
    return None