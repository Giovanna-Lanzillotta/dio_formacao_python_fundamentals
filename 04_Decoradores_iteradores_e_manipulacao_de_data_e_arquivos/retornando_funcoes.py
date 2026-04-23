# Retornando funções de funções

def calcular(operacao):

    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    
    def dividir(a, b):
        return a / b
    
    def mensagemErro(*args): 
        print("Esta opção não existe")
        return None
    

    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "*":
        return multiplicar
    elif operacao == "/":
        return dividir
    else:
        return mensagemErro
    

resultadoSoma = calcular("+")(1, 3)
print(resultadoSoma)

resultadoSubtracao = calcular("-")(8, 2)
print(resultadoSubtracao)

resultadoMultiplicao = calcular("*")(9, 4)
print(resultadoMultiplicao)

resultadoDivisao = calcular("/")(90, 5)
print(resultadoDivisao)

resultadoErro = calcular("?")(1, 7)
print(resultadoErro)