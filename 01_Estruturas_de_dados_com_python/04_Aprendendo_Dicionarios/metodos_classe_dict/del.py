# MÉTODOS DA CLASSE DICT - del

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444"},
}

print(contatos)
# {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1111-1111'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '2222-2222'}, 'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-3333'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '4444-4444'}}

del contatos["guilherme@gmail.com"]['telefone']

print(contatos) 
# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '2222-2222'}, 'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-3333'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '4444-4444'}}

del contatos["chappie@gmail.com"]

print(contatos)
# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '2222-2222'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '4444-4444'}}

del contatos["giovanna@gmail.com"]["nome"]
print(contatos)
# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'telefone': '2222-2222'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '4444-4444'}}

del contatos
print(contatos) # NameError: name 'contatos' is not defined