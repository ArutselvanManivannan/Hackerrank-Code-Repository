# https://www.hackerrank.com/challenges/calendar-module/problem

# from datetime import datetime
import calendar

month, date, year = [int(i) for i in input().split()]

# d = datetime(year, month, date).strftime("%A").upper()
# print(d)

print(calendar.day_name[calendar.weekday(year, month, date)].upper())

# github.com/ArutselvanManivannan
