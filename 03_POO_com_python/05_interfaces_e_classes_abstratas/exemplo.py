# Variávesi de classe e Variáveis de instância

class Estudante:
    escola = "DIO"


    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    

    def __str__(self):
        return f"{self.nome} ({self.numero} - {self.escola})"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2= Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# aluno_1.numero = 3
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie",3)
mostrar_valores(aluno_1, aluno_2,aluno_3)

