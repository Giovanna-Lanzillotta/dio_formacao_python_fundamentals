# MÉTODOS DA CLASSE DICT - {}.clear

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444"},
}

print(contatos) # {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1111-1111'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '2222-2222'}, 'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-3333'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '4444-4444'}}

contatos.clear()

print(contatos)  # {}