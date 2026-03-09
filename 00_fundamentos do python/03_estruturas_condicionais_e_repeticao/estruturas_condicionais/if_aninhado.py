# if aninhado

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 450


if conta_normal :
    if saldo >= saque:
        print("Saque realizado com sucesso!! 💰")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!!! 🧾")
    else:
        print("Não foi possivel realizar o saque!!!❌")

elif conta_especial:
    print("Conta especial selecionada 💡")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!! 💸")
    else:
        print("Saldo insuficiente!! ❌")
else:
    print(" ⚠ Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!!")


nome_de_usuario = "admin"
senha = "123"

usuario = input("😐 Digite seu nome de usuário: ")

if usuario == nome_de_usuario:
    senha_digitada = input("🔒 Digite sua senha: ")
    if senha_digitada == senha:
        print(f"☀ Bem vindo {nome_de_usuario}")
    else:
        print("❌senha incorreta")
else:
    print("🔎 Usuário não encontrado")


