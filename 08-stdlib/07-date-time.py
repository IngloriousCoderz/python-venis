from datetime import datetime
from datetime import date

today = date.today()  # ?
today  # 'datetime.date(2022, 5, 30)'
print(today)  # '2022-05-30'
print(today.strftime('%d/%m/%Y'))  # '30/05/2022'

birth_date = date(1982, 10, 17)
age = today - birth_date  # age is a timedelta
print(age.days / 365)  # years are not readily available


now = datetime.today()
print(now)
print(now.strftime('%d/%m/%Y %H:%M'))
