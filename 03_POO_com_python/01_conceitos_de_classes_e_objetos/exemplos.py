# Exemplo de construtores e destrutores

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe... 🐶")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self):
        print(" 🚮 Removendo a instância da classe.")
    
    
    def falar(self):
        print("au au 🗯")


def criar_cachorro(): 
    cao = Cachorro("Zeus", "branco e preto", False)
    print(cao.nome)


# cachorro1 = Cachorro("Toby","marrom")
# cachorro2 = Cachorro("Chappie", "amarelo")
# cachorro2.falar()

criar_cachorro()