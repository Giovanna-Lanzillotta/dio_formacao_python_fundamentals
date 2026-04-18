# HERANÇA SIMPLES

class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self. numero_de_rodas = numero_de_rodas

    
    def ligar_motor(self):
       print("Ligando o motor...🚥") 

    
    def __str__(self):

        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    
    def __init__(self,cor, placa, numero_de_rodas, carregado):
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f"{'✅ sim' if self.carregado else ' ❌ não'} estou carregado!")



moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()
print(moto)


carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()
print(carro)


caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)