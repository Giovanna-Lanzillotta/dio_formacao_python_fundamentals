# Formatando e convertendo datas com strftime e strptime
# Exemplo de código

import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M")) # 25/04/2026 17:26

# Convertendo strings para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M") # 2023-07-20 15:30:00
print(d)