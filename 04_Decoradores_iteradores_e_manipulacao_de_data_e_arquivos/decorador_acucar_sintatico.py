# Decorador açúcar sintático
# O python permite que você use decoradores de maneira mais simples com o símbolo @

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função 😎")
        funcao()
        print("Faz algo depois de executar a função 😁")

    return envelope
    

@meu_decorador
def ola_mundo():
    print("😜 Olá mundo!")



ola_mundo()