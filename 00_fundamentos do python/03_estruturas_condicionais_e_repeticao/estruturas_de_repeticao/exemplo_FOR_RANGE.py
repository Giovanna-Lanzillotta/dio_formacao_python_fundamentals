# estruturas de repetição

# comando FOR

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() # adiciona uma quera de linha
    print("Executa uma quebra de linha")


# Função range

# range(stop) -> range object
# range (start,stop[, step]) -> range object

lista = list(range(4))
print(lista) # 0 1 2 3


print("\nListando numeros de 1 a 10")
# Utilizando range com for
for numero in range(0,11):
    print(numero, end=" ") # 0 2 3 4 5 6 7 8 9 10

print("\nTabuada do cinco")
# Exibindo tabuada do cinco
for number in range (0, 51, 5):
    print(number, end=" ") #0 5 10 15 20 25 30 35 40 45 50



# FOR range com break
print("\nFOR range com break")

for numero in range(100):

    if numero == 20:
        break

    print(numero, end=" ")



# FOR range com continue
#Não exibe o numero 20
print("\nFOR range com continue")

for numero in range(100):

    if numero == 20:
        continue

    print(numero, end=" ")