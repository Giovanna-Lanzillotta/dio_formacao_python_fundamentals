
class meuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
    


# for i in meuIterador(numeros=[1, 2, 3]):
#     print(i)


for i in meuIterador(numeros=[38, 13, 11]):
    print(i)