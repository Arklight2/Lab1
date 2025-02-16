import re


def count_vc_cv_pairs(s):
    vowels = "аеёиоуыэюяaeiouy"
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"

    vc_count = len(re.findall(f'[{vowels}][{consonants}]', s, re.IGNORECASE))
    cv_count = len(re.findall(f'[{consonants}][{vowels}]', s, re.IGNORECASE))

    return abs(vc_count - cv_count)


def sort_strings_by_vc_difference(strings):
    return sorted(strings, key=count_vc_cv_pairs)


n = int(input("Введите количество строк: "))
strings = [input(f"Введите строку {i + 1}: ") for i in range(n)]

sorted_strings = sort_strings_by_vc_difference(strings)
print("Отсортированные строки:")
print("\n".join(sorted_strings))