import datetime
from datetime import datetime
monday1 = 0
months = range(1,13)
for year in range(2018, 2029):
    for month in months:
        if datetime(year, month, 8).weekday() == 0:
            monday1 += 1
print(monday1)