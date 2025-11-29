def busqueda_secuencial(arr, elemento):
    """
    Algoritmo de búsqueda secuencial (o lineal).
    Busca un elemento recorriendo la lista de principio a fin.

    Args:
        arr: Lista donde buscar (puede estar ordenada o no)
        elemento: Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe

    Complejidad: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == elemento:
            return i
    return -1


def busqueda_secuencial_todas_ocurrencias(arr, elemento):
    """
    Búsqueda secuencial que devuelve todas las ocurrencias de un elemento.

    Args:
        arr: Lista donde buscar
        elemento: Elemento a buscar

    Returns:
        list: Lista de índices donde se encuentra el elemento
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == elemento:
            indices.append(i)
    return indices


def busqueda_secuencial_ordenada(arr, elemento):
    """
    Búsqueda secuencial optimizada para listas ordenadas.
    Se detiene si encuentra un elemento mayor al buscado.

    Args:
        arr: Lista ordenada donde buscar
        elemento: Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe

    Complejidad: O(n) en el peor caso, pero más eficiente en promedio
    """
    for i in range(len(arr)):
        if arr[i] == elemento:
            return i
        elif arr[i] > elemento:
            return -1  # El elemento no existe
    return -1


if __name__ == "__main__":
    # Ejemplos de uso
    print("--- Búsqueda Secuencial Simple ---")
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista:", lista)

    elemento = 22
    resultado = busqueda_secuencial(lista, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    elemento = 100
    resultado = busqueda_secuencial(lista, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    print("\n--- Búsqueda de Todas las Ocurrencias ---")
    lista_con_duplicados = [5, 3, 7, 3, 9, 3, 1]
    print("Lista:", lista_con_duplicados)

    elemento = 3
    indices = busqueda_secuencial_todas_ocurrencias(lista_con_duplicados, elemento)
    if indices:
        print(f"Elemento {elemento} encontrado en los índices: {indices}")
    else:
        print(f"Elemento {elemento} no encontrado")

    print("\n--- Búsqueda Secuencial en Lista Ordenada ---")
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Lista ordenada:", lista_ordenada)

    elemento = 9
    resultado = busqueda_secuencial_ordenada(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    elemento = 8
    resultado = busqueda_secuencial_ordenada(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado (se detuvo la búsqueda al encontrar un elemento mayor)")
