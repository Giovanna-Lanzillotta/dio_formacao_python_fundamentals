# Estruturas de repetição 

# Comando WHILE

opcao = -1

while opcao !=0:
    opcao = (int(input("\n[1] Sacar \n [2] Extrato \n [0] Sair \n: ")))

    if opcao == 1:
        print("💸💸Sacando...")
    elif opcao == 2:
        print("🧾🧾Exibindo o extrato...")



# WHILE/ELSE

option = -1

while option !=0:
    option = (int(input("Digite uma das opções:\n[1] Sacar \n [2] Extrato \n [0] Sair \n: ")))

    if option == 1:
        print("💸💸Sacando...")
    elif option == 2:
        print("🧾🧾Exibindo o extrato...")
else:
    print("💰💰 Obrigado por usar nosso sistema bancário, até logo!!")



# Estruturs repetição break

numero = True

while numero != 0:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)




while True:
    num = int(input("Digite um número: "))

    if num % 2 != 0:
        print("numero IMPAR")
        break

    print(f"o numero digitado foi: {num} e é PAR")



while True:
    number = int(input("Digite un numero: "))

    if number == 10:
        break

    if number % 2 == 0:
        continue

    print(number)