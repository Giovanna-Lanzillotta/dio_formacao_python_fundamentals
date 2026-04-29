import os
import shutil
from pathlib import Path

#print(__file__)

ROOT_path = Path(__file__).parent
# print(ROOT_path.parent)

#os.mkdir("novo-diretorio")
# os.mkdir(ROOT_path / "novo-diretorio") comentar depois de criar, pois dá erro

# arquivo = open('novo-arquivo.txt')
arquivo = open(ROOT_path / "novo.txt", "w")
arquivo.close()

# os.rename(ROOT_path/"novo.txt", ROOT_path/"alterado.txt")

# os.remove(ROOT_path / "alterado.txt")

shutil.move(ROOT_path / "novo.txt", ROOT_path / "novo-diretorio" / "novo.txt")