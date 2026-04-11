# MÉTODOS DA CLASSE DICT - in

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444"},
}

print("guilherme@gmail.com" in contatos) # True
print("meugui@gmail.com" in contatos) # False
print("idade" in contatos["guilherme@gmail.com"]) # False
print("telefone" in contatos["giovanna@gmail.com"]) # True
