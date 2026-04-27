# timezone

# Exenmplo de código 

#pip install pytz

from datetime import datetime, timezone, timedelta
import pytz

# Criando datetimec com timezone
d = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)  # 2026-04-27 10:46:21.770443-03:00


data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)  # 2026-04-27 19:30:56.780732+02:00



data_oslo = datetime.now(timezone(timedelta(hours=2))) # 2026-04-27 19:47:51.936908+02:00
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3))) # 2026-04-27 14:47:51.936908-03:00

print(data_oslo)
print(data_sao_paulo)


# Outro exemplo de código

# Criando datetime com timezona
a = datetime.now(timezone(timedelta(hours=-3), "BRT"))
print(a) # 2026-04-27 14:51:17.825785-03:00

# Convertendo para outro timezone
a_utc = a.astimezone(timezone.utc)
print(a_utc) # 2026-04-27 17:52:09.216737+00:00