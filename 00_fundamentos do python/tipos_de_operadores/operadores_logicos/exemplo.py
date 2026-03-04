# OPERADORES LÓGICOS

saldo = 1000
saque = 200
limite = 100

# operador E 
print("------operador AND------")
print(f"true and true é {True and True}")
print(f"true and false é {True and False}")
print(f"false and false é {False and False}")

# true and false
print(saldo >= saque and saldo <= limite) # False

# true and true
print(saldo >= saque and saldo >= limite) # True



# Operador OU
print("\n------operador OR------")
print(f"true or true é {True or True}")
print(f"true or false é {True or False}")
print(f"false or true é {False or True}")
print(f"false or false é {False or False}")

# true or false
print(saldo >= saque or saldo <= limite) # True

# false or true
print(saldo <= saque or saldo >= limite) # True

# true or true
print(saldo >= saque or saldo >= limite) # True

# false or false
print(saldo <= saque or saldo <= limite) # False



# Operador NOT
# negaçao de false é true
print("\n------operador NOT------")

contatos_emergencia = []

print(not 1000 > 1500) #true

print(not contatos_emergencia) #true

print(not "saque 1500;") #false

print( not "") #true



# PARÊNTESES
print("\n------Parênteses------")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo>= saque) #true

print((saldo >=saque and saque <= limite) or (conta_especial and saldo >= saldo)) #true
