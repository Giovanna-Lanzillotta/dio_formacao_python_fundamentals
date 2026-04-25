# timedelta

from datetime import datetime, timedelta, date, time

tipo_carro = 'M' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'🚗 O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'🚙 O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'🚐 O carro chegou: {data_atual} e ficará pronto às {data_estimada}')


# Diminuindo 1 dia do dia de hoje(2026-04-25)
print(date.today() - timedelta(days=1)) # 2026-04-24


# TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.timedelta'
# print(time(10, 19, 20)- timedelta(hours=1))
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado) # 2023-07-25 09:19:20
print(resultado.time()) # 09:19:20


print(datetime.now().date()) # 2026-04-25

# Adicionando 7 semanas a partir do dia de hoje(2026-04-25)
print(date.today() + timedelta(weeks=7)) # 2026-06-13