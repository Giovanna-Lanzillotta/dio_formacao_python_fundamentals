# DECORADORES

def dizer_oi(nome):
    return f"Oi {nome}"
 

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"


def mensagem_para_giovanna(funcao_mensagem):
    return funcao_mensagem("Giovanna")


print(mensagem_para_giovanna(dizer_oi))
print(mensagem_para_giovanna(incentivar_aprender))