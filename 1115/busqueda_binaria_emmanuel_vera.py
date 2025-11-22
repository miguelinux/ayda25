def busqueda_binaria(aguja, pajar, izquierda=None, derecha=None):
    # Por default 'izquierda' y 'derecha' adoptan el tamaño completo de pajar
    if izquierda is None:
        izquierda = 0               # El valor default de izquierda es 0
    if derecha is None:
        derecha = len(pajar) - 1    # El valor default de derecha es igual al index del ultimo elemento del pajar

    # CASO BASE
    if izquierda > derecha:
        return None                 # La aguja no esta en el pajar

    mid = (izquierda + derecha) // 2
    # CASO BASE
    if aguja == pajar[mid]:
        return mid                  # La aguja ha sido encontrada en el pajar
    elif aguja < pajar[mid]:        # CASO RECURSIVO
        return busqueda_binaria(aguja, pajar, izquierda, mid - 1)
    elif aguja > pajar[mid]:        # CASO RECURSIVO
        return busqueda_binaria(aguja, pajar, mid + 1, derecha)

print(busqueda_binaria(16, [1, 4, 8, 11, 13, 16, 19, 19]))
