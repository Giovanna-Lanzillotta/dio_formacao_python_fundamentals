# Tratamento de exceções em manipulação de arquivos

from pathlib import Path

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError:
    print("Arquivo não encontrado")

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!!!!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")



ROOT_PATH = Path(__file__).parent

# try:
#     arquivo2 = open(ROOT_PATH / "novo-diretorio")
# except (IsADirectoryError, PermissionError) as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")