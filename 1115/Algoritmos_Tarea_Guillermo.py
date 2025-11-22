# Algoritmo de Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    """
    La función realiza una búsqueda binaria en una lista ordenada.
    Retorna el índice del objetivo si se encuentra, o -1 si no se encuentra.
    """
    # Definir los índices de inicio y fin
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        # Calcular el índice del medio
        medio = (inicio + fin) // 2

        # Verificar si el valor en el medio es el objetivo
        if lista[medio] == objetivo:
            return medio  # Si lo encontramos, devolvemos la posición
        elif lista[medio] < objetivo:
            # Si el valor en medio es menor, buscar en la mitad derecha
            inicio = medio + 1
        else:
            # Si el valor en medio es mayor, buscar en la mitad izquierda
            fin = medio - 1
    
    return -1  # Si no encontramos el objetivo, devolver -1


# Algoritmo de Búsqueda Secuencial
def busqueda_secuencial(lista, objetivo):
    """
    La función realiza una búsqueda secuencial en la lista.
    Retorna el índice del objetivo si se encuentra, o -1 si no se encuentra.
    """
    # Recorrer toda la lista de izquierda a derecha
    for i in range(len(lista)):
        # Si encontramos el elemento, devolver su índice
        if lista[i] == objetivo:
            return i
    return -1  # Si no encontramos el elemento, devolver -1


# Ejemplo de uso de ambos algoritmos

if __name__ == "__main__":
    # Lista de ejemplo para Búsqueda Binaria
    lista_binaria = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo_binario = 7
    resultado_binario = busqueda_binaria(lista_binaria, objetivo_binario)

    if resultado_binario != -1:
        print(f"Búsqueda Binaria: Elemento encontrado en el índice {resultado_binario}")
    else:
        print("Búsqueda Binaria: Elemento no encontrado")

    # Lista de ejemplo para Búsqueda Secuencial
    lista_secuencial = [2, 4, 6, 8, 10, 12, 14]
    objetivo_secuencial = 8
    resultado_secuencial = busqueda_secuencial(lista_secuencial, objetivo_secuencial)

    if resultado_secuencial != -1:
        print(f"Búsqueda Secuencial: Elemento encontrado en el índice {resultado_secuencial}")
    else:
        print("Búsqueda Secuencial: Elemento no encontrado")
