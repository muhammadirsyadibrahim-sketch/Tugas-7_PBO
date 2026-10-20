# ==========================================
# Python sleep()
# ==========================================

# Contoh 1: Contoh penggunaan sleep() di Python
import time

time.sleep(2)

print("Tunggu sampai 2 detik.")
print()

# Contoh 2: Metode sleep()
import time

print("Dicetak langsung.")
time.sleep(2.4)
print("Dicetak setelah 2,4 detik.")
print()

# Contoh 3: Membuat Jam Digital di Python
import time

while True:
    # mengambil waktu lokal saat ini sebagai data terstruktur
    current_time = time.localtime()

    # memformat waktu dalam format 12 jam dengan AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", current_time)

    print(formatted_time)
    time.sleep(1)
    print()