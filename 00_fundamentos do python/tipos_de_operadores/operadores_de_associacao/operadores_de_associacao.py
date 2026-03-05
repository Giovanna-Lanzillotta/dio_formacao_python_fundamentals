frutas = ["limão", "uva", "laranja"]

print(f"abacaxi in frutas?? {'abacaxi' in frutas}") #false
print(f"laranja in frutas?? {'laranja' in frutas}") #true
print(f"limão in frutas?? {'limão' in frutas}") #true

# Case sensitive é um termo da informática que indica que um sistema, 
# linguagem de programação diferencia letras maiúsculas de minúsculas 
print("------ case sensitive ------")
print(f"LARANJA in frutas?? {'LARANJA' in frutas}") #false
print(f"LaRaNjA in frutas?? {'LaRaNjA' in frutas}") #false

print("------ NOT IN ------")
print(f"limão not in frutas?? {'limão' not in frutas}") #false
print(f"melancia not in frutas?? {'melancia' not in frutas}") #true


print("------ usando AND / OR ------")
print(f"limão in frutas and laranja in frutas?? {'limão' in frutas and 'laranja' in frutas}") #true
print(f"banana in frutas and laranja in frutas?? {'banana'in frutas and 'laranja' in frutas}") #false

print(f"banana in frutas or laranja in frutas?? {'banana'in frutas or 'laranja' in frutas}") #true
print(f"morango in frutas or abacaxi in frutas?? {'morango'in frutas or 'abacaxi' in frutas}") #false

print(f"banana in frutas and abacaxi not in frutas?? {'banana'in frutas and 'abacaxi' not in frutas}") #false
print(f"uva in frutas or abacaxi not in frutas?? {'uva'in frutas or 'abacaxi' not in frutas}") #true

print("--------------------")

curso = "Curso de Python"

print(f"Python in curso ?? {'Python' in curso}") #true
print(f"JavaScript in curso ?? {'JavaScript' in curso}") #false
print(f"Java not in curso ?? {'Java' not in curso}") #true