def linear_search(lst, target):
    """
    Functional linear search:
    Pure recursive function. No mutation, no loops.
    """
    return _search_rec(lst, target, 0)

def _search_rec(lst, target, index):
    """Recursive helper: scans the list one element at a time."""
    # Base case: end of list → not found
    if index == len(lst):
        return -1
    # If match → return index
    if lst[index] == target:
        return index
    # Otherwise continue scanning
    return _search_rec(lst, target, index + 1)


# ----------- Example usage ------------

numbers = [5, 10, 3, 8, 15, 20]
target = 8

result = linear_search(numbers, target)

print(f"Encontrado en el índice {result}" if result != -1 else "No encontrado")

