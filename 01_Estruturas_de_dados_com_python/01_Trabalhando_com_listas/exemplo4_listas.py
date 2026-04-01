# Modificando valores versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)


nums = [1, 2, 3, 4, 5]
dobro = []

for num in nums:
    dobro.append(num * 2)

print(dobro)


# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)


nums = [55, 7, 89, 12, 40, 15]
triplo = [num * 3 for num in nums]
print(triplo)