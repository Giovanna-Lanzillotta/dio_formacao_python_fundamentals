# MÉTODOS DA CLASSE DICT - {}.keys

contatos = {
    "guilherme@gmail.com": {"nome" : "Guilherme", "telefone": "3333-2221"}
}

print(contatos.keys()) # dict_keys(['guilherme@gmail.com'])



lista = {
    "cores" : {"azul","amarelo","verde","vermelho"},
    "frutas" : {"abacaxi","banana","uva"},
    "doces" : {"bolo","pudim","brigadeiro"}
}

print(lista.keys()) # dict_keys(['cores', 'frutas', 'doces'])