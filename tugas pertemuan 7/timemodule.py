# ==========================================
# Python time Module
# ==========================================

# Contoh 1: Fungsi time.time()
import time

# mengambil waktu saat ini dalam detik sejak epoch
seconds = time.time()

print("Detik sejak epoch =", seconds)
print()

# Contoh 2: Fungsi time.ctime()
import time

# detik yang berlalu sejak epoch
seconds = 1672215379.5045543

# mengubah waktu dalam detik sejak epoch ke format yang mudah dibaca
local_time = time.ctime(seconds)

print("Waktu lokal:", local_time)
print()

# Contoh 3: Fungsi time.sleep()
import time

print("Dicetak langsung.")
time.sleep(2.4)
print("Dicetak setelah 2,4 detik.")
print()

# Contoh 4: Fungsi time.localtime()
import time

result = time.localtime(1672214933)

print("result:", result)
print("\ntahun:", result.tm_year)
print("tm_hour:", result.tm_hour)
print()

# Contoh 5: Fungsi time.gmtime()
import time

result = time.gmtime(1672214933)

print("result:", result)
print("\ntahun:", result.tm_year)
print("tm_hour:", result.tm_hour)
print()

# Contoh 6: Fungsi time.mktime()
import time

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

# mengubah time_tuple menjadi detik sejak epoch
seconds = time.mktime(time_tuple)

print(seconds)
print()

# Contoh 7: Fungsi time.asctime()
import time

# time tuple
t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Hasil:", result)
print()

# Contoh 8: Fungsi time.strftime()
import time

# tanggal dan waktu saat ini
named_tuple = time.localtime()

# memformat waktu
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)
print()

# Contoh 9: Fungsi time.strptime()
import time

# string waktu
time_string = "14 July, 2023"

# parsing string waktu
result = time.strptime(time_string, "%d %B, %Y")

print(result)
print()