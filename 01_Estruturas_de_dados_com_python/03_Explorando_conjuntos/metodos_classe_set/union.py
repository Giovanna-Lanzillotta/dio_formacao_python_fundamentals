# MÉTODOS DA CLASSE SET - {}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")

print(f"União do conjunto a com conjunto b: {conjunto_a.union(conjunto_b)}")  # {1, 2, 3, 4}



conjunto_c = {"azul", "amarelo", "vermelho"}
conjunto_d = {"verde", "rosa", "amarelo"}

print(f"Conjunto c: {conjunto_c}")
print(f"Conjunto d: {conjunto_d}")

print(f"União do conjunto c com conjunto d: {conjunto_c.union(conjunto_d)}") # {'vermelho', 'azul', 'rosa', 'amarelo', 'verde'}