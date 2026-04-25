from datetime import date, datetime, time

data = date(2023,7, 10)
print(data) # 2023-07-10


# Retorna a data local atual
hoje = date.today()
print(hoje) # 2026-04-25


# Exibe (Ano, Mês, Dia, Hora, Minuto, Segundo)
data_hora = datetime(2023,7, 10, 10, 30, 20)
print(data_hora) # 2023-07-10 10:30:20  (yyyy-mm-dd hh:mm:ss)


# Caso eu não informe a hora, minuto, segundo
data_sem_hora = datetime(2023,12, 25)
print(data_sem_hora) # 2023-12-25 00:00:00


data_hora_hoje = datetime.today()
print(data_hora_hoje) # 2026-04-25 16:22:32.893546


hora = time(10, 20, 0)
print(hora) # 10:20:00

hora2 = time(12, 30, 40)
print(hora2) # 12:30:40