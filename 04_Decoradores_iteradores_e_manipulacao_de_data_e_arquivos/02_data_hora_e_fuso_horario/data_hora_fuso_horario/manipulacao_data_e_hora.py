# Manipulação de datas e horas

# Exemplo de código
import datetime

# Criando data e hora
d = datetime.datetime(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d) # 2023-07-26 13:45:00