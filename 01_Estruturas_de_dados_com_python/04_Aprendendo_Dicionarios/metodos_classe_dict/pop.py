# MÉTODOS DA CLASSE DICT - {}.pop
# remove uma chave do dicionário

contatos = {
    "guilherme@gmail.com": {"nome" : "Guilherme", "telefone": "3333-2221"}
}

print(contatos.pop("guilherme@gmail.com")) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

print(contatos) # {}

print(contatos.pop("guilherme@gmail.com", {})) # {}




lista = {
    "cores" : {"azul","amarelo","verde","vermelho"},
    "frutas" : {"abacaxi","banana","uva"},
    "doces" : {"bolo","pudim","brigadeiro"}
}

lista.pop("frutas")

print(lista)

print(lista.pop("frutas",["?"])) # ['?']