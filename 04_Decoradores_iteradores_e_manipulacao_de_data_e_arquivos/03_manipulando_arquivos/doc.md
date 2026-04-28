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