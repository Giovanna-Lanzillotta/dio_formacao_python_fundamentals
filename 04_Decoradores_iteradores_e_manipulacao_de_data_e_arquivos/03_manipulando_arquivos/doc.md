# Manipulando arquivos

## Abrindo e fechando arquivos

O primeiro passso para manipular arquivo é abri-li usando a função `open()` e quando terminar de trabalhar com o arquvo, usamos a função `close()` pra liberar recursos.

### Exemplo de código:

```python
file = open("example.txt", "r")
# ... fazemos algo com o arquivo ...
file.close()
```

### Modos de abertura de arquivo

- somente leitura (`'r'`)
- gravação (`'w'`)
- anexar (`'a'`)

### Exemplo de código:

```python
# Para ler um arquivo
file = open('example.txt', 'r')

# Para escrever em um arquivo
file = open('example.txt', 'w')

# Para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')
```

### Leitura de arquivo

- `read()`
- `readline()`
- `readlines()`

### Exemplo de código
### Método read:

```python
# Ler todo o conteúdo do arquivo de uma vez
file = open('example.txt', 'r')
print(file.read())
file.close()
```

### Método readline e readlines

- método `readline()` - Lê uma linha por vez.
- método `readlines()` - Retorna uma lista onde cada elemento é uma linha do arquivo.

### Exemplo de código

```Python
# Ler todo o conteúdo do arquivo de uma vez
file = open('example.txt', 'r')
print(file.readline())
file.close()
```

## Escrevendo em um arquivo

-  Pode ser usado `write()` ou `writelines()` para escrever emum arquivo.
*Lembre-se:* De abrir o arquivo no modo correto.

### Exemplo de código

```python
file = open('example.txt', 'w')
file.write("Olá,mundo!")
file.close()
```

## Gerenciando arquivos e diretórios

- Podemos criar, renomear e xcluir arquivos e diretórios usando os módulos `'os'` e `'shutil'`.

### Exemplo de código
```python
import os
import shutil

# Criar um diretório
os.mkdir("exemplo")

# Renomear um arquivo
os.rename("old.text", "new.text")

# Remover um arquivo
os.remove("unwanted.txt")

# Mover um arquivo
shutil.move("source.txt", "destination.txt")
```

## Tratamente de exceções em manipulação de arquivos

### Exceções mais comuns

- **FileNotFoundError:** Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.

- **PermissionError:** Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.

- **IOError:** Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.

- **UnicodeDecodeError:** Lançada quando ocorre um erro a tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.

- **UnicocodeEncodeError:** Lançada quando ocoore um erro ao tentar codificae dados em uma determinada codificação ao gravar em um arquivo de texto.

- **IsADirectoryError:** Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.

### Exemplo de código
```python
try:
    file = open('non_existent_file.txt','r')
except FileNotFoundError:
    print("Arquivo não encontrado.")
```