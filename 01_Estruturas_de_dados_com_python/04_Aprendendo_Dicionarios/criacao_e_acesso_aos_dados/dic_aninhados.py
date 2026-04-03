# Dicionários aninhados

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444", "extra":{"a":1}},
}

print(contatos["giovanna@gmail.com"]["telefone"])  # 2222-2222
print(contatos["chappie@gmail.com"]["nome"])  #Chappie


telefone = contatos["melaine@gmail.com"]["telefone"]
print(telefone)


extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)