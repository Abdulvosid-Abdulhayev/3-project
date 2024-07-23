import time

def print_current_date():
    current_time = time.localtime()
    formatted_time = time.strftime("Today:\n%A %d %B %Y %H:%M:%S\n%d.%m.%Y", current_time)
    print(formatted_time)

# Misol
print_current_date()
