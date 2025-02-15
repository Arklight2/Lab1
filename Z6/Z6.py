import re

def count_russian_characters(text):
    return len(re.findall(r'[а-яА-Я]', text))
text = input("Введите строку: ")
print("Количество русских символов:", count_russian_characters(text))