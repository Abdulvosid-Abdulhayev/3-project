import datetime

def week_day_number(date_string):
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return date.isoweekday()

# Misol
print(week_day_number("2023-07-18"))  # 1 - Dushanba
