import random

def busqueda_binaria(lista, objetivo):
    """Busca 'objetivo' en 'lista' usando búsqueda binaria."""
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        valor_mitad = lista[mitad]

        if valor_mitad == objetivo:
            return mitad  # Encontrado
        elif objetivo < valor_mitad:
            fin = mitad - 1  # Buscar en la mitad izquierda
        else:
            inicio = mitad + 1  # Buscar en la mitad derecha

    return -1  # No encontrado


# Generar una lista aleatoria de 100 números entre 1 y 1000
lista = [random.randint(1, 1000) for _ in range(100)]

# Ordenar la lista (requisito de la búsqueda binaria)
lista.sort()

print("Lista generada y ordenada:")
print(lista)

# Solicitar al usuario el número a buscar
objetivo = int(input("Ingresa el número que deseas buscar: "))

# Ejecutar la búsqueda binaria
resultado = busqueda_binaria(lista, objetivo)

# Mostrar resultado
if resultado != -1:
    print(f"El número {objetivo} fue encontrado en la posición {resultado}.")
else:
    print(f"El número {objetivo} NO se encuentra en la lista.")
