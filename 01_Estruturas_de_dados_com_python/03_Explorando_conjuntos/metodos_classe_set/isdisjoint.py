# MÉTODOS DA CLASSE SET - {}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")
print(f"Conjunto c: {conjunto_c}")

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False