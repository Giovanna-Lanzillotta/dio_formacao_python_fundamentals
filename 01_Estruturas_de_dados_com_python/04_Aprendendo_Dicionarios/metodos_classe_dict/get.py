# MÉTODOS DA CLASSE DICT - {}.get

contatos = {
    "guilherme@gmail.com": {"nome" : "Guilherme", "telefone": "3333-2221"}
}

# print(contatos["chave"]) # KeyError: 'chave'

print(contatos.get("chave")) # None

print(contatos.get("chave", {})) # {}

print(contatos.get("guilherme@gmail.com", {}))  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

