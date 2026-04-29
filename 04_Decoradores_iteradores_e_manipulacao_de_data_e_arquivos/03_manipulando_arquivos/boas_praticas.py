# Boas práticas na manipulação de arquivos

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
#     1 / 0

# print(arquivo.read())



# try:
#     with open(ROOT_PATH / "llorem.txt", "r") as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#     print(f"❗❗Erro ao abrir o arquivo: {exc}")



# try:
#      with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#          arquivo.write("Aprendendo a manipular arquivos utilizando python")
# except IOError as exc:
#     print(f"❗❗❗Erro ao abrir o arquivo: {exc}")


try:
     with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
         print(arquivo.read())
except IOError as exc:
    print(f"❗❗❗Erro ao abrir o arquivo: {exc}")