from datetime import date, datetime

now = datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time)

december = "5 December, 2019"
time_december = datetime.strptime(december, "%d %B, %Y")
print(time_december)

new_year = date(year=2025, month=1, day=1)
today = date(year=2024, month=7, day= 16)
print(new_year - today)

epoch = date(year=1970, month=1, day= 1)
print(today - epoch)

#This module can be used in anything that requires dates and hours, including stuff involving deadlines or keeping track of the time for any reason