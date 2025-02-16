import re

def count_words(s):
    return len(re.findall(r'\b[a-zA-Zа-яА-Я]+\b', s))

def sort_strings_by_word_count(strings):
    return sorted(strings, key=count_words)


n = int(input("Введите количество строк: "))
strings = [input(f"Введите строку {i+1}: ") for i in range(n)]

sorted_strings = sort_strings_by_word_count(strings)
print("Отсортированные строки по количеству слов:")
print("\n".join(sorted_strings))
