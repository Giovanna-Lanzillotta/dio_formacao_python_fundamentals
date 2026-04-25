def mensagem(nome):
    print("🍪 Executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("🍟 Executando mensagem longa")
    return f"Olá tudo bem com você {nome}"

def executar(funcao, nome):
    print("🍦 Execuntado executar")
    return funcao(nome)


# executar(mensagem,"Joao")
print(executar(mensagem, 'joao'))
print(executar(mensagem_longa, 'Maria'))