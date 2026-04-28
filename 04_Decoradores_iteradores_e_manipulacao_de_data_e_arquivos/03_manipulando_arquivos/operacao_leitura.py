arquivo = open(
    r"C:\Users\Giovanna\Desktop\workspace\dio\formacao_python_fundamentals\04_Decoradores_iteradores_e_manipulacao_de_data_e_arquivos\03_manipulando_arquivos\lorem.txt",
    "r"
)
print(arquivo.read()) # retorna a string inteira do código
print(arquivo.readline()) # retorna somente a primerira linha
print(arquivo.readlines())

for linha in arquivo.readline():
    print(linha)

for linha in arquivo.readlines():
    print(linha)

for linha in arquivo.read():
    print(linha)

# Dica
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()


