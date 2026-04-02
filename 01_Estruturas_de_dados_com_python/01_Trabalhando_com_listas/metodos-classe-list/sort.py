# Métodos da classe list - [].sort

# Ordem alfabética
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)  # ['c', 'csharp', 'java', 'js', 'python']


# Ordem alfabética no sentido reverso
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)  # ['python', 'js', 'java', 'csharp', 'c']


# Ordem crescente pelo tamanho da palavra
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x : len(x))
print(linguagens)  # ['c', 'js', 'java', 'python', 'csharp']


# Ordem decrescente pelo tamanho da palavra
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x : len(x), reverse=True)
print(linguagens)  # ['c', 'js', 'java', 'python', 'csharp']