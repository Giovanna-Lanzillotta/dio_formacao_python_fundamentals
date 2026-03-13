# Conhecendo métodos úteis da classe string

# Maiúscula, minúscula e título

curso = "PYtHon"

print(f"Maiúscula: {curso.upper()}")
print(f"Minúscula: {curso.lower()}")
print(f"Título: {curso.title()}")

nome = "gIovanNA"

print(f"Meu nome é: {nome.upper()}")
print(f"Meu nome é: {nome.lower()}")
print(f"Meu nome é: {nome.title()}")



# Eliminando espaços e branco

curso = "   Python "

print(curso.strip())  #espaço em ambos
print(curso.lstrip()) #espaço da esquerda
print(curso.rstrip()) #espaço da direita


frase = "    O rato roeu a roupa do rei de roma.     "

print(f"Texto normal: {frase}🐀")
print(f"Texto espaço em ambos: {frase.strip()}🐀")
print(f"Texto espaço esquerda: {frase.lstrip()}🐀")
print(f"Texto espaço direita: {frase.rstrip()}🐀")


texto = "   Olá mundo!   "

print((texto) + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")  
print(texto.rstrip() + ".")


# Junções e centralização

curso = "Python"

print(curso.center(10,"#"))  #center(numero de caracteres,opcional-> caracter que quer colocar nestes espaços)
print(curso.center(8,"🐍"))
print(curso.center(12,"*").upper())
print(curso.center(12,"🎯").lower())


print(".".join(curso))
print("✨".join(curso))
print(" 💎 ".join(curso).upper())


print("_".join(curso).center(20,"🐍"))
print("-".join((curso).center(20,"🐍").upper()))