# # Esrutura Condicional


# # IF

saldo = 2000.0
saque = float(input("Informe o valor do saque:  "))

if saldo >= saque:
    print("Realizando saque! 💰")

if saldo < saque:
    print("Saldo insuficiente! ❌")


# # IF/ELSE

saldo = 10000.0
saque = float(input("Informe o valor do saque:  "))

if saldo >= saque:
    print("Realizando saque! 💰")

else:
    print("Saldo insuficiente! ❌")



# IF/ELIF/ELSE

import sys

extrato = 1000
opcao = int(input(("Informe uma opção [1] Sacar \[2] Extrato: ")))

if opcao == 1:
    valor = float(input(" 💰Informe a quantia para o saque: "))
    print(f"Saindo o valor de {valor} 💸")

elif opcao == 2:
    print("Exibindo o extrato.... 🧾")
    print(f"Você tem...{extrato}")

else:
    sys.exit("Opção inválida ❌")