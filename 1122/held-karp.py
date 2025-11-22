#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import itertools

def held_karp(distancia_matriz):
    """
    Implementa el algoritmo de Held-Karp para resolver el TSP.
    Problema del Viajante de Comercio.
    
    Argumentos:
        distancia_matriz (list de list): Matriz de adyacencia donde
                                        distancia_matriz[i][j] es el costo de ir de i a j.
    
    Retorna:
        int: El costo de la ruta más corta del TSP.
    """
    n = len(distancia_matriz)
    
    # 1. Inicialización de la Programación Dinámica (PD)
    # La tabla DP almacenará:
    # dp[(S, j)] = costo mínimo para visitar el conjunto de ciudades S, 
    #              terminando en la ciudad j.
    # El conjunto S se representa como un 'bitmask' (máscara de bits).
    # Tamaño de la tabla: 2^n * n
    dp = {} 
    
    # Caso base: El costo de ir del nodo inicial (0) a cualquier otro nodo j 
    # cuando solo se ha visitado {0, j}.
    # La máscara de bits para {0, j} es (1 << 0) | (1 << j)
    for j in range(1, n):
        # bitmask: 1 al inicio y en la posición 'j'
        mask = (1 << 0) | (1 << j) 
        dp[(mask, j)] = distancia_matriz[0][j]
        
    # 2. Iteración de la PD
    # La iteración se realiza sobre el tamaño del conjunto S, desde 3 hasta n.
    # Un conjunto de tamaño 'k' tiene 1 bit encendido en la posición 0 (inicio)
    # y 'k-1' bits encendidos en las posiciones 1 a n-1.
    for k in range(3, n + 1):
        # Itera sobre todas las posibles 'bitmasks' S de tamaño k
        # El bit 0 debe estar siempre encendido (ya que la ruta comienza en 0).
        # Los bits del 1 al n-1 representan las ciudades intermedias.
        
        # itertools.combinations genera todas las combinaciones de índices de ciudades
        # que NO incluyen el nodo inicial (0).
        for subset_indices in itertools.combinations(range(1, n), k - 1):
            
            # Construye la bitmask S (incluye el nodo inicial 0)
            mask = 1 | sum(1 << i for i in subset_indices)
            
            # Itera sobre todos los posibles nodos finales 'j' en el conjunto S
            for j in subset_indices:
                # El nodo 'j' debe estar encendido en la máscara
                
                # La máscara S sin el nodo 'j' (S - {j})
                prev_mask = mask & ~(1 << j) 
                
                # Inicializa el costo mínimo para llegar a 'j' a través de S
                min_cost = float('inf')
                
                # El penúltimo nodo 'i' debe estar en S - {j} y no puede ser 0
                for i in subset_indices:
                    if i != j:
                        # Si la solución previa (S - {j}, i) existe:
                        if (prev_mask, i) in dp:
                            costo_previo = dp[(prev_mask, i)]
                            costo_actual = costo_previo + distancia_matriz[i][j]
                            min_cost = min(min_cost, costo_actual)
                
                # Almacena el resultado para el estado (mask, j)
                dp[(mask, j)] = min_cost

    # 3. Paso Final (Regreso al Origen)
    # El conjunto S final es el conjunto de todas las ciudades.
    final_mask = (1 << n) - 1 # Máscara con todos los bits encendidos (0, 1, ..., n-1)
    
    # Itera sobre todos los posibles penúltimos nodos 'j' (1 a n-1)
    min_final_cost = float('inf')
    
    for j in range(1, n):
        # Costo para llegar al penúltimo nodo j a través de todas las ciudades (final_mask)
        costo_a_j = dp.get((final_mask, j), float('inf'))
        
        # Costo de volver del penúltimo nodo 'j' al nodo inicial '0'
        costo_total = costo_a_j + distancia_matriz[j][0] 
        
        min_final_cost = min(min_final_cost, costo_total)
        
    return min_final_cost

# --- Ejemplo de Uso ---

# Ciudades: 0, 1, 2, 3 (n=4)
# Matriz de distancias: distancia[i][j] = costo de i a j
# Nota: Para un TSP simétrico (distancia[i][j] = distancia[j][i]), 
# la matriz sería simétrica.

distancias = [
    # 0,  1,  2,  3
    [0, 10, 15, 20], # de 0
    [5, 0, 9, 10],   # de 1
    [6, 13, 0, 12],  # de 2
    [8, 8, 9, 0]     # de 3
]

costo_minimo = held_karp(distancias)
print(f"El costo mínimo de la ruta del Viajante de Comercio es: {costo_minimo}")
