# INTERPOLAÇÃO DE VARIÁVEIS

# Old style %

nome = "Giovanna"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print("Olá me chamo %s. Eu tenho %d anos de idade,trabalho como %s e estou matriculada no curso de %s."%(nome, idade, profissao,linguagem))


nome = input("Qual é o seu nome??? ")
idade = int(input("Qual é a sua idade?? "))
profissao = input("Qual é a sua profissão?? ")
curso = input("Qual curso você esta fazendo???? ")

print("Olá me chamo %s. Eu tenho %d anos de idade,trabalho como %s e estou matriculada no curso de %s."%(nome, idade, profissao,curso))



# Método format

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}".format(nome,idade,profissao,linguagem))


print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}".format(nome,idade,profissao,linguagem))


nome = "João"
idade = 25
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


pessoa = {
    "nome": "Maria",
    "idade": 34,
    "profissao": "Programadora",
    "linguagem": "Java"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}".format(**pessoa))



# f-string

nome = "Bia"
idade = 23
profissao = "Desenvolvedora"
linguagem = "HTML e CSS"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")



# Formatar strings com f-string

PI = 3.14159

print(f"O valor de PI: {PI:.2f}")
print(f"O valor de PI: {PI:10.2f}")


print(f"O valor de {PI:.3f} * 2 = {(PI*2):.3f}")
print(f"O valor de {PI:.3f} * 2 = {(PI*2):10.3f}")