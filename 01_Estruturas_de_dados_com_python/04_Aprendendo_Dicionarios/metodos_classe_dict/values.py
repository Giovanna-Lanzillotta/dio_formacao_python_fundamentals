# MÉTODOS DA CLASSE DICT - {}.values

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "1111-1111"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "2222-2222"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "3333-3333"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "4444-4444"},
}

print(contatos.values())
# dict_values([{'nome': 'Guilherme', 'telefone': '1111-1111'}, {'nome': 'Giovanna', 'telefone': '2222-2222'}, {'nome': 'Chappie', 'telefone': '3333-3333'}, {'nome': 'Melaine', 'telefone': '4444-4444'}])

lista = {
    "cores" : {"azul","amarelo","verde","vermelho"},
    "frutas" : {"abacaxi","banana","uva"},
    "doces" : {"bolo","pudim","brigadeiro"}
}


print(lista.values())
# dict_values([{'amarelo', 'azul', 'vermelho', 'verde'}, {'banana', 'abacaxi', 'uva'}, {'bolo', 'brigadeiro', 'pudim'}])