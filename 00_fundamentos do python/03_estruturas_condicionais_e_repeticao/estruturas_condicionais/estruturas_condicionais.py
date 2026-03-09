MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

#if

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH. 🚗")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH⚽")



# if else

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH. 🚙")

else:
    print("Ainda não pode tirar a CNH 🪁")



numero = int(input("Digte um numero:"))

if numero % 2 == 0:
    print("é par")

else:
    print("é impar")


# if elif

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH. 🚘")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas 📘")
else:
    print("Ainda não pode tirar a CNH 🎮")



id = int(input("Digite a sua idade: "))

if id >= 18:
    print("Voto obrigatório 🗳")
elif id >= 16 and id < 18:
    print("Voto facultativo 🗳")
else:
    print("Ainda não pode votar 👶")
