# MÉTODOS DA CLASSE DICT - {}.setdefault

contatos = {"nome" : "Guilherme", "telefone": "3333-2221"}

print(contatos) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contatos.setdefault("nome", "Giovanna") 
print(contatos) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contatos.setdefault("idade",28)
print(contatos) # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28