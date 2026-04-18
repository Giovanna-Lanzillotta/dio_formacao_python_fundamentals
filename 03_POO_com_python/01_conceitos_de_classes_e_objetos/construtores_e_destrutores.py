# Construtores e Destrutores

#  __init__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado



# __del__

class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro
del c