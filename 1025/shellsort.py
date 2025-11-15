#!usr/bin/python3

#shellsort
import random
import time

elementos = 100
inicio = 0
fin = 100


def ordenar(arr):
    size = len(arr)

    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j=i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j-= gap
            arr[j]=temp
        gap //=2
    
    return arr



def main():

    lista=[random.randint(inicio,fin) for _ in range(elementos)]
    shellsort = lista.copy()

    print("lista original", lista)

    tiempo_inicio = time.time()
    ordenar(shellsort)
    tiempo_fin = time.time()

    duracion = tiempo_fin - tiempo_inicio
    print(f"shellsort se ejecuto en: {duracion:.6f} segundos.")
    
    print("lista ordenada", shellsort)
    

if __name__ == "__main__":
    main()