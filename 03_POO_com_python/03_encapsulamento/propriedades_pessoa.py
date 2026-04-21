class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    

    @property
    def nome(self):
        return self._nome
    

    # @nome.setter
    # def nome(self, value):
    #     # logica para modificar nome
    #     pass


    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento
    

# outro modo de fazer
    # def get_nome(self):
    #     return self.nome
    

    # def get_idade(self):
    #     return 2026 - self._ano_nascimento



pessoa = Pessoa("Giovanna", 2001)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# pessoa2 = Pessoa("Guilherme", 1994)
# print(f"Nome: {pessoa2.get_nome()} \tIdade: {pessoa2.get_idade()}")