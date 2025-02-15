import re

def find_min_integer(text):
    numbers = list(map(int, re.findall(r'[-]?\d+', text)))
    return min(numbers) if numbers else None
text = input("Введите строку: ")
print("Минимальное целое число в строке:", find_min_integer(text))