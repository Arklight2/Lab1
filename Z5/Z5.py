import re
from datetime import datetime

def is_valid_date(day, month, year):
    month_map = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
                 "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    try:
        datetime(year, month_map[month], day)
        return True
    except ValueError:
        return False

def find_dates(text):
    pattern = r'\b(\d{1,2})\s(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s(\d{4})\b'
    matches = re.findall(pattern, text)
    valid_dates = [" ".join(match) for match in matches if is_valid_date(int(match[0]), match[1], int(match[2]))]
    return valid_dates

# Ввод строки от пользователя
text = input("Введите строку: ")
dates = find_dates(text)
print("Найденные корректные даты:", dates)