# MÉTODOS DA CLASSE SET - {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")

print(f"Interseção do conjunto a com conjunto b: {conjunto_a.intersection(conjunto_b)}") #  {2, 3}



conjunto_c = {"azul", "amarelo", "vermelho"}
conjunto_d = {"verde", "rosa", "amarelo"}

print(f"Conjunto c: {conjunto_c}")
print(f"Conjunto d: {conjunto_d}")

print(f"Interseção do conjunto c com conjunto d: {conjunto_c.intersection(conjunto_d)}") # {'amarelo'}