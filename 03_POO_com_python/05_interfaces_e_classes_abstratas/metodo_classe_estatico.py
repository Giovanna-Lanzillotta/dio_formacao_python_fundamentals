# Interfaces e Classes Abstratas com Python
# Métodos de classe e Métodos estático

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


# método de classe
    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2026 - ano
        return cls(nome, idade)
        # return Pessoa(nome, idade)


# método estático
    @staticmethod
    def e_maior_idade(idade):
        # return idade >= 18
       return "Maior de idade" if idade >= 18 else "Menor de idade"




# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)


p2 = Pessoa.criar_apartir_data_nascimento(1994, 3, 21, "Guilherme")
print(p2.nome, p2.idade) # Guilherme 32

print(Pessoa.e_maior_idade(18)) # True
print(Pessoa.e_maior_idade(28)) # True
print(Pessoa.e_maior_idade(8))  # False