def busqueda_binaria(arr, elemento):
    """
    Algoritmo de búsqueda binaria.
    Busca un elemento en una lista ordenada dividiendo repetidamente
    el espacio de búsqueda a la mitad.

    Args:
        arr: Lista ordenada donde buscar
        elemento: Elemento a buscar

    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe

    Complejidad: O(log n)
    """
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == elemento:
            return medio
        elif arr[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def busqueda_binaria_recursiva(arr, elemento, izquierda=0, derecha=None):
    """
    Algoritmo de búsqueda binaria recursiva.

    Args:
        arr: Lista ordenada donde buscar
        elemento: Elemento a buscar
        izquierda: Índice inicial
        derecha: Índice final

    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe
    """
    if derecha is None:
        derecha = len(arr) - 1

    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if arr[medio] == elemento:
        return medio
    elif arr[medio] < elemento:
        return busqueda_binaria_recursiva(arr, elemento, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, elemento, izquierda, medio - 1)


if __name__ == "__main__":
    # Ejemplos de uso
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print("Lista ordenada:", lista_ordenada)
    print("\n--- Búsqueda Binaria Iterativa ---")

    elemento = 7
    resultado = busqueda_binaria(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    elemento = 20
    resultado = busqueda_binaria(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    print("\n--- Búsqueda Binaria Recursiva ---")

    elemento = 13
    resultado = busqueda_binaria_recursiva(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")

    elemento = 8
    resultado = busqueda_binaria_recursiva(lista_ordenada, elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en el índice {resultado}")
    else:
        print(f"Elemento {elemento} no encontrado")
