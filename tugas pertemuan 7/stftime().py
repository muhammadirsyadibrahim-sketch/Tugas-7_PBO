# ==========================================
# Python strftime()
# ==========================================

# Contoh 1: Datetime ke string menggunakan strftime()
from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print("tahun:", year)

month = now.strftime("%m")
print("bulan:", month)

day = now.strftime("%d")
print("tanggal:", day)

time = now.strftime("%H:%M:%S")
print("waktu:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("tanggal dan waktu:", date_time)
print()

# Contoh 2: Membuat string dari sebuah timestamp
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Objek tanggal waktu:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)
print()

# Contoh 3: Tanggal dan waktu sesuai locale
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Output 1:", d)

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%X")
print("Output 3:", d)
print()