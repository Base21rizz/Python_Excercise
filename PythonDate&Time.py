from datetime import datetime

# Getting datetime Information
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(now)
timestamp = now.timestamp()
print(timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Without Formatting Date Output Using strftime
""" new_year = datetime(2026, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(f'{day}/{month}/{year}, {hour}:{minute}') """

# Formatting Date Output Using strftime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H,%M,%S")
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time now:", time_two)

# String to Time Using strptime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
