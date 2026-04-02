# MÉTODOS DA CLASSE SET - {}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")

print(conjunto_a.issuperset(conjunto_b))  # False
print(conjunto_b.issuperset(conjunto_a))  # True