# MÉTODOS DA CLASSE DICT - {}.copy

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444"},
}

print(contatos) 

copia = contatos.copy()

copia["guilherme@gmail.com"] = {"nome" : "Gui"}

print(contatos["guilherme@gmail.com"]) # {'nome': 'Guilherme', 'telefone': '1111-1111'}
print(copia["guilherme@gmail.com"])  # {'nome': 'Gui'}
