# Python Mendapatkan Tanggal dan Waktu Saat Ini

# Contoh 1: Mendapatkan tanggal hari ini
from datetime import date

today = date.today()
print("Tanggal hari ini:", today)
print()

# Contoh 2: Tanggal saat ini dalam berbagai format
from datetime import date

today = date.today()

# dd/mm/YY (tanggal/bulan/tahun)
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Bulan dalam teks, tanggal dan tahun
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y (bulan/tanggal/tahun)
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Singkatan bulan, tanggal dan tahun
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
print()

# Contoh 3: Mendapatkan tanggal dan waktu saat ini di Python
from datetime import datetime

# objek datetime berisi tanggal dan waktu saat ini
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S (tanggal/bulan/tahun jam:menit:detik)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("tanggal dan waktu =", dt_string)
print()