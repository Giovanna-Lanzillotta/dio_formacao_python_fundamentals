# Parâmetro especiais - Keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0",combustivel="Gasolina")
# válido
# Palio 1999 ABC-1234 Fiat 1.0 Gasolina

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido
# TypeError: criar_carro() takes 0 positional arguments but 3 positional arguments (and 3 keyword-only arguments) were given