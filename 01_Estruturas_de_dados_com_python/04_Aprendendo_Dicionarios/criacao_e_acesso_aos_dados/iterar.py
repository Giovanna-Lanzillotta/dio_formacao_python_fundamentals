# ITERAR DICIONÁRIOS

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444", "extra":{"a":1}},
}

for chave in contatos:
    print(chave, contatos[chave])


for chave,valor in contatos.items():
    print(chave, valor)



menu = {
    "salgados": [
        {"nome": "coxinha", "preco": 6.00},
        {"nome": "pão de queijo", "preco": 5.00}
    ],
    "doce" : {"nome": "sorvete","preco": 3.00},
}


for opcao in menu:
    print(opcao, menu[opcao])