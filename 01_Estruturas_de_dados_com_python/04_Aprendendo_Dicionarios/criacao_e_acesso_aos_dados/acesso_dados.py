# Acesso aos dados

dados = {"nome": "Giovanna", "idade":28, "telefone":"3333-3333"}

print(dados) # {'nome': 'Giovanna', 'idade': 28, 'telefone': '3333-3333'}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "1111-1111"

print(dados) # {'nome': 'Maria', 'idade': 18, 'telefone': '1111-1111'}




pedido = {
    "comida":"hamburguer",
    "bebida":"refrigrante",
    "acompanhamento": "batata-frita",
    "sobremesa": "sorvete"
      }

print(pedido) 
# {'comida': 'hamburguer', 'bebida': 'refrigrante', 'acompanhamento': 'batata-frita', 'sobremesa': 'sorvete'}

print(pedido["comida"])
print(pedido["bebida"])
print(pedido["acompanhamento"])
print(pedido["sobremesa"])

pedido["entrada"] = "pastel"

print(pedido)
# {'comida': 'hamburguer', 'bebida': 'refrigrante', 'acompanhamento': 'batata-frita', 'sobremesa': 'sorvete', 'entrada': 'pastel'}