# Herança Múltipla

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# **kwargs permitem que uma função receba um número ilimitado de argumentos nomeados (como um dicionário).

# classe Mamifero estende de Animal
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return 'Mamifero'

# classe Ave estende de Animal
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
    def __str__(self):
        return 'ave 42'



# classe Cachorro estende de Mamifero
class Cachorro(Mamifero):
    pass


# classe Gato estende de Mamifero
class Gato(Mamifero):
    pass


# classe Leao estende de Mamifero
class Leao(Mamifero):
    pass
# Um Mixin é uma classe projetada para fornecer métodos específicos a outras classes por meio de herança múltipla, mas que não foi feita para ser instanciada sozinha.
class FalarMixin:
    def falar(self):
       return "Oi, estou falando 💬"


# classe Onitorrinco estende de Mamifero e ave
class Onitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo,nro_patas):
        # __mro__ : Exibe a Ordem de Resolução de Métodos (Method Resolution Order).
        # print(Onitorrinco.__mro__)
        print(Onitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

    def __str__(self):
        return 'Onitorinco'


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

onitorrinco = Onitorrinco(nro_patas=2, cor_pelo="vermelho",cor_bico="laranja")
print(onitorrinco)
print(onitorrinco.falar())