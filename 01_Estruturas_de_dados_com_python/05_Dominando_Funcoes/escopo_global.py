# Escopo global
# NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA

salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)

    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500,lista)
print(salario_com_bonus) # 2500
print(lista) # [1]
# print(salario_bonus(500)) # 2500