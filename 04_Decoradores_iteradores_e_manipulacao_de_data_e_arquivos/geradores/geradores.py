
def meu_gerador():
# A palavra reservada yield em Python é utilizada para transformar uma função em um gerador (generator)
    # yield 1
    texto = 'python'
    yield texto


for i in meu_gerador():
    print(i)