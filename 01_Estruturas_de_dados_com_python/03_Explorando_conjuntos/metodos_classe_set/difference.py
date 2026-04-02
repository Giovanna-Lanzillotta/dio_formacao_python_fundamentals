# MÉTODOS DA CLASSE SET - {}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(f"Conjunto a: {conjunto_a}")
print(f"Conjunto b: {conjunto_b}")

print(f"A diferença do conjunto a com conjunto b: {conjunto_a.difference(conjunto_b)}")  # {1}
print(f"A diferença do conjunto b com conjunto a: {conjunto_b.difference(conjunto_a)}")  # {4}



conjunto_c = {"azul", "amarelo", "vermelho"}
conjunto_d = {"verde", "rosa", "amarelo"}

print(f"Conjunto c: {conjunto_c}")
print(f"Conjunto d: {conjunto_d}")

print(f"A diferença do conjunto c com conjunto d: {conjunto_c.difference(conjunto_d)}")  # {'azul', 'vermelho'}
print(f"A diferença do conjunto d com conjunto c: {conjunto_d.difference(conjunto_c)}") # {'verde', 'rosa'}  
