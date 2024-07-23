import calendar

def print_month_calendar(year, month):
    print(calendar.month(year, month))

def print_year_calendar(year):
    print(calendar.calendar(year))

# Misol
print_month_calendar(2024, 7)
print_year_calendar(2024)
