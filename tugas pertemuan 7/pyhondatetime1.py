# ==========================================
# Python datetime
# ==========================================

# Contoh 1: Mendapatkan Tanggal dan Waktu Saat Ini
import datetime

# mengambil tanggal dan waktu saat ini
now = datetime.datetime.now()

print(now)
print()

# Contoh 2: Mendapatkan Tanggal Saat Ini
import datetime

# mengambil tanggal saat ini
current_date = datetime.date.today()

print(current_date)
print()

# Atribut-atribut pada modul datetime
import datetime

print(dir(datetime))
print()


# ==========================================
# Python datetime.date Class
# ==========================================

# Contoh 3: Objek date untuk merepresentasikan sebuah tanggal
import datetime

d = datetime.date(2022, 12, 25)
print(d)
print()

# Mengimpor hanya kelas date
from datetime import date

d = date(2022, 12, 25)
print(d)
print()

# Contoh 4: Mendapatkan tanggal saat ini menggunakan today()
from datetime import date

# today() untuk mendapatkan tanggal saat ini
todays_date = date.today()

print("Tanggal hari ini =", todays_date)
print()

# Contoh 5: Mendapatkan tanggal dari sebuah timestamp
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Tanggal =", timestamp)
print()

# Contoh 6: Menampilkan tahun, bulan, dan hari hari ini
from datetime import date

# objek date dari tanggal hari ini
today = date.today()

print("Tahun saat ini:", today.year)
print("Bulan saat ini:", today.month)
print("Hari saat ini:", today.day)
print()


# ==========================================
# Python datetime.time Class
# ==========================================

# Contoh 7: Objek time untuk merepresentasikan waktu
from datetime import time

# time(jam = 0, menit = 0, detik = 0)
a = time()
print(a)

# time(jam, menit, dan detik)
b = time(11, 34, 56)
print(b)

# time(jam, menit, dan detik)
c = time(hour=11, minute=34, second=56)
print(c)

# time(jam, menit, detik, mikrodetik)
d = time(11, 34, 56, 234566)
print(d)
print()

# Contoh 8: Menampilkan jam, menit, detik, dan mikrodetik
from datetime import time

a = time(11, 34, 56)

print("Jam =", a.hour)
print("Menit =", a.minute)
print("Detik =", a.second)
print("Mikrodetik =", a.microsecond)
print()


# ==========================================
# The datetime.datetime Class
# ==========================================

# Contoh 9: Objek datetime di Python
from datetime import datetime

# datetime(tahun, bulan, hari)
a = datetime(2022, 12, 28)
print(a)

# datetime(tahun, bulan, hari, jam, menit, detik, mikrodetik)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)
print()

# Contoh 10: Menampilkan tahun, bulan, jam, menit, dan timestamp
from datetime import datetime

a = datetime(2022, 12, 28, 23, 55, 59, 342380)

print("Tahun =", a.year)
print("Bulan =", a.month)
print("Jam =", a.hour)
print("Menit =", a.minute)
print("Timestamp =", a.timestamp())
print()


# ==========================================
# Python datetime.timedelta Class
# ==========================================

# Contoh 11: Selisih antara dua objek date/datetime
from datetime import datetime, date

# menggunakan date()
t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)

t3 = t1 - t2

print("t3 =", t3)

# menggunakan datetime()
t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)

print("Tipe t3 =", type(t3))
print("Tipe t6 =", type(t6))
print()

# Contoh 12: Selisih antara dua objek timedelta
from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)

t3 = t1 - t2

print("t3 =", t3)
print()

# Contoh 14: Durasi waktu dalam satuan detik
from datetime import timedelta

t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("Total detik =", t.total_seconds())
print()


# ==========================================
# Python strptime() Method
# ==========================================

from datetime import datetime

date_string = "25 December, 2022"
print("date_string =", date_string)

# menggunakan strptime() untuk membuat objek date
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print()


# ==========================================
# Handling timezone in Python
# ==========================================

from datetime import datetime
import pytz

local = datetime.now()
print("Lokal:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
print()