# CONVERSÃO DE TIPOS

# INTEIRO PARA FLOAT
preco = 10
print(preco)
preco = float(preco)
print(preco)

preco = 10/2
print(preco)

# FLOAT PARA INTEIRO
preco = 10.00
print(preco) 

preco = int(preco)
print(preco)

#CONVERSAO POR DIVISAO
preco = 10
print(preco)

print(preco/2)

print(preco//2)


# NUMÉRO PARA STRING
preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

#ERRO DE CONVERSÃO
# preco = "python"
# print(float(preco))
# saída:   print(float(preco))
#           ^^^^^^^^^^^^
# ValueError: could not convert string to float: 'python'

print("CONVERTENDO TIPOS")
print(int(1.97348726))
print(int("10"))
print(float("10.10"))
print(float(100))

print(type(str(10.10)))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100/2)
print(100//2)