saldo = 1000
limite = 500

print(saldo is limite)  # false
print(saldo is not limite) # true


saldo = 2000
limite = 2000

print(saldo is limite)  # true
print(saldo is not limite) # false

print("\n")
bola = "amarela"
print("A bola é amarela")
print("--------------------")
print(f"A bola é azul é {bola is 'azul'}")  # false
print(f"A bola não é azul é {bola is not 'azul'}")  # true
print(f"A bola é amarela é {bola is 'amarela'}")  # true