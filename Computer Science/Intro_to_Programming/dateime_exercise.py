from datetime import datetime

birthday = datetime(1994, 2, 15, 4, 25, 12)

print(birthday.year, birthday.month, birthday.day)
print(birthday.hour, birthday.weekday())

now_time = datetime.now()
print(now_time)

date_difference = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(date_difference)

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date, parsed_date.year, parsed_date.month)

date_string  = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)