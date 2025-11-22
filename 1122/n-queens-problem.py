def n_queens_brute_force(n):
    """
    Encuentra todas las soluciones al problema de las N reinas
    usando fuerza bruta (generando todas las permutaciones)
    Complejidad: O(n!)
    """
    from itertools import permutations
    
    solutions = []
    # Cada permutación representa una colocación de reinas
    for permutation in permutations(range(n)):
        if is_valid_solution(permutation):
            solutions.append(permutation)
    
    return solutions

def is_valid_solution(placement):
    """
    Verifica si ninguna reina se ataca mutuamente
    """
    n = len(placement)
    for i in range(n):
        for j in range(i + 1, n):
            # Verificar diagonales
            if abs(placement[i] - placement[j]) == abs(i - j):
                return False
    return True

# Ejemplo para 4 reinas
print(f"Soluciones para 4 reinas: {n_queens_brute_force(4)}")