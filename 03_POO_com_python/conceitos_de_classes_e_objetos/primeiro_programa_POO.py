# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe:
# cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzina,parar e correr. Adicione esses comportamentos

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, andando=False, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.andando = andando
        self.aro = aro
    
    def buzinar(self):
        print("bi bi 📢")

    def parar(self):
        self.andando = False
        print("parado 🛑")

    def correr(self):
        self.andando = True
        print("correndo 🚴")


    def __str__(self):
        return f" 🚲 Bicicleta : cor:{self.cor}, modelo:{self.modelo}, ano:{self.ano}, valor:{self.valor} 🚲"


    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

bicicleta_1 = Bicicleta("vermelha", "caloi", 2000, 599.99, True)
bicicleta_2 = Bicicleta("azul", "caloi", 1998, 399.99)
bicicleta_3 = Bicicleta("verde", "caloi", 2010, 699.99)

bicicleta_1.parar()
bicicleta_2.buzinar()
bicicleta_3.correr()

print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)
print(bicicleta_2.cor, bicicleta_2.modelo)

Bicicleta.buzinar(bicicleta_3)

print(bicicleta_1)