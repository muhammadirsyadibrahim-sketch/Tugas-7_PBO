# Contoh 1: Waktu saat ini menggunakan objek datetime
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Waktu Saat Ini =", current_time)
print()

# Contoh 2: Waktu saat ini menggunakan modul time
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
print()

# Contoh 3: Waktu saat ini di zona waktu tertentu (pakai zoneinfo)
from datetime import datetime
from zoneinfo import ZoneInfo

# Ambil waktu saat ini di New York
tz_NY = ZoneInfo('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("Waktu NY:", datetime_NY.strftime("%H:%M:%S"))

# Ambil waktu saat ini di London
tz_London = ZoneInfo('Europe/London')
datetime_London = datetime.now(tz_London)
print("Waktu London:", datetime_London.strftime("%H:%M:%S"))
print()