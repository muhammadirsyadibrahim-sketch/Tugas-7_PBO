# ==========================================
# Konversi Timestamp ke Datetime dan Sebaliknya
# ==========================================

# Contoh 1: Python timestamp ke datetime
from datetime import datetime

# timestamp adalah jumlah detik sejak 1970-01-01
timestamp = 1545730073

# mengubah timestamp menjadi objek datetime di zona waktu lokal
dt_object = datetime.fromtimestamp(timestamp)

# menampilkan objek datetime dan tipenya
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))
print()

# Contoh 2: Python datetime ke timestamp
from datetime import datetime

# tanggal dan waktu saat ini
now = datetime.now()

# mengubah dari datetime ke timestamp
ts = datetime.timestamp(now)

print("Timestamp =", ts)
print()