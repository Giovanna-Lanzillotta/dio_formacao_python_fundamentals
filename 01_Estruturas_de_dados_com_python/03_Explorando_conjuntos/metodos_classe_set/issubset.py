# MÉTODOS DA CLASSE SET - {}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")


print(conjunto_a.issubset(conjunto_b))  # True
print(conjunto_b.issubset(conjunto_a))  # False