# FUNÇÕES

def exibir_mensagem():
    print("olá mundo!") 


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}") 

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!") 

exibir_mensagem() # olá mundo!
exibir_mensagem_2(nome="Giovanna") # Seja bem vindo Giovanna
exibir_mensagem_3()  # Seja bem vindo Anônimo!
exibir_mensagem_3(nome="Chappie") # Seja bem vindo Chappie!