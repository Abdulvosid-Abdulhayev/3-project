import os
import calendar

def save_year_calendar_html(year):
    html_calendar = calendar.HTMLCalendar(calendar.SUNDAY)
    with open('calendar.html', 'w') as f:
        f.write(html_calendar.formatyear(year))

# Fayl yo'qligini tekshirish
file_path = 'calendar.html'
file_exists = os.path.isfile(file_path)

# Agar fayl yo'q bo'lsa, yaratish va saqlash
if not file_exists:
    save_year_calendar_html(2024)

# Yaratilgandan keyin fayl mavjudligini qayta tekshirish
file_exists_after = os.path.isfile(file_path)
print(file_exists_after)  # True yoki False

# Fayl yoqilganini ko'rsatish
if file_exists_after:
    print(f"The file '{file_path}' has been created and saved successfully.")
else:
    print(f"The file '{file_path}' could not be created.")
