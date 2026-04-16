# Objetos de primerira classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

def test(a, b):
    return a * 2 + b * 3

exibir_resultados(10, 10, somar) # O resultado da operação 10 + 10 = 20
exibir_resultados(5, 9, somar) # O resultado da operação 5 + 9 = 14

exibir_resultados(12, 8, subtrair) # O resultado da operação é = 4
exibir_resultados(8, 10, subtrair) # O resultado da operação é = -2

exibir_resultados(1, 2, test) #  resultado da operação é = 8

exibir_resultados(3, 2, multiplicar) # O resultado da operação é = 6
exibir_resultados(-1, 5, multiplicar) # O resultado da operação é = -5


op = somar

print(op(1,23)) # 24