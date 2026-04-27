# strftime e strptime

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2023-10-20 10:20'
mascara_ptbr = '%d/%m/%Y'
mascara_ptbr_com_hora = '%d/%m/%Y %H'
mascara_ptbr_com_semana_abreviado = '%d/%m/%Y %a'
mascara_ptbr_com_semana = '%d/%m/%Y %A'
mascara_ptbr_com_mes = '%d de %B de %Y '


print(data_hora_atual.strftime(mascara_ptbr))  # 27/04/2026
print(data_hora_atual.strftime(mascara_ptbr_com_hora))  # 27/04/2026 10
print(data_hora_atual.strftime(mascara_ptbr_com_semana_abreviado)) # 27/04/2026 Mon
print(data_hora_atual.strftime(mascara_ptbr_com_semana)) # 27/04/2026 Monday
print(data_hora_atual.strftime(mascara_ptbr_com_mes)) # 27 de April de 2026 

print(type(data_hora_str))  # <class 'str'>



mascara_en = '%Y-%m-%d %H:%M'

print(datetime.strptime(data_hora_str, mascara_en)) # 2023-10-20 10:20:00

print(type(datetime.strptime(data_hora_str, mascara_en))) # <class 'datetime.datetime'>