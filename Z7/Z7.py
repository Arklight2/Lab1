import re

def find_lowercase_latin(text):
    return set(re.findall(r'[a-z]', text))
text = input("Введите строку: ")
print("Используемые строчные латинские буквы:", find_lowercase_latin(text))