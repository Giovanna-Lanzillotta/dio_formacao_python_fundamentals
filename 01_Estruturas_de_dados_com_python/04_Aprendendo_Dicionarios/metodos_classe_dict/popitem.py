# MÉTODOS DA CLASSE DICT - {}.popitem

contatos = {
    "guilherme@gmail.com": {"nome" : "Guilherme", "telefone": "3333-2221"}
}

print(contatos.popitem()) # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

# print(contatos.popitem()) KeyError: 'popitem(): dictionary is empty'


lista = {
    "cores" : {"azul","amarelo","verde","vermelho"},
    "frutas" : {"abacaxi","banana","uva"},
    "doces" : {"bolo","pudim","brigadeiro"}
}

print(lista) # {'cores': {'verde', 'vermelho', 'azul', 'amarelo'}, 'frutas': {'uva', 'abacaxi', 'banana'}, 'doces': {'pudim', 'bolo', 'brigadeiro'}}

lista.popitem()
print(lista) # {'cores': {'verde', 'vermelho', 'azul', 'amarelo'}, 'frutas': {'uva', 'abacaxi', 'banana'}}