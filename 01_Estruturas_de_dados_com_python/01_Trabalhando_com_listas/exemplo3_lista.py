# Compreensão de Listas - filtrar elementos


# filtro versão 1
numeros = [1,30,21,2,9,65,34]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


print(pares)


#filtro versão 2
numeros = [2,33,27,6,7,69,36]
num_pares = [numero for numero in numeros if numero % 2 == 0]
print(num_pares)