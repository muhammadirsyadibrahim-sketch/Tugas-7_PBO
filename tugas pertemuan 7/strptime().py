# ==========================================
# Python strptime()
# ==========================================

# Contoh 1: String ke objek datetime
from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("tipe date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("tipe date_object =", type(date_object))
print()

# Contoh 2: String ke objek datetime dengan dua format
from datetime import datetime

dt_string = "12/11/2018 09:15:32"

# Menganggap tanggal dalam format dd/mm/yyyy
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Menganggap tanggal dalam format mm/dd/yyyy
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)
print()

# ValueError pada strptime()
from datetime import datetime

date_string = "12/11/2018"
date_object = datetime.strptime(date_string, "%d/%m/%Y")

print("date_object =", date_object)
print()