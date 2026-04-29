# TRABALHANDO COM ARQUIVOS CSV

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "w",newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")



try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[0], row[1])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="",  encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"🔸 ID: {row[COLUNA_ID]}")
            print(f"🔹 NOME: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

try:
   with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["id"], row["nome"])
except IOError as exc:
    print(f"Erro ao criar arquivo : {exc}")


try:
   with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"🟢 ID: {row['id']}")
            print(f"🟣 NOME: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar arquivo : {exc}")