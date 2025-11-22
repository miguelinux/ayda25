import random

def busqueda_secuencial(lista, objetivo):
    """Busca 'objetivo' en 'lista' usando búsqueda secuencial."""
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice  # Número encontrado
    return -1  # No encontrado


# Generar una lista aleatoria de 100 números entre 1 y 1000
lista = [random.randint(1, 1000) for _ in range(100)]

print("Lista generada:")
print(lista)

# Solicitar al usuario el número a buscar
objetivo = int(input("Ingresa el número que deseas buscar: "))

# Ejecutar la búsqueda secuencial
resultado = busqueda_secuencial(lista, objetivo)

# Mostrar el resultado
if resultado != -1:
    print(f"El número {objetivo} fue encontrado en la posición {resultado}.")
else:
    print(f"El número {objetivo} NO se encuentra en la lista.")
