from datetime import datetime

def check_date(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# Misol
print(check_date("2024-01-01", "2024-07-18"))  # Misol: 199 kun
