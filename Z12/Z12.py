from collections import Counter
import string


def char_frequency_quadratic_deviation(s):
    s = s.lower()
    char_counts = Counter(s)
    total_chars = sum(char_counts.values())

    if not total_chars:
        return float('inf')

    most_common_char, most_common_count = char_counts.most_common(1)[0]
    alphabet_freq = 1 / len(string.ascii_lowercase)
    actual_freq = most_common_count / total_chars
    return (actual_freq - alphabet_freq) ** 2


def sort_strings_by_quadratic_deviation(strings):
    return sorted(strings, key=char_frequency_quadratic_deviation)



n = int(input("Введите количество строк: "))
strings = [input(f"Введите строку {i + 1}: ") for i in range(n)]

sorted_strings = sort_strings_by_quadratic_deviation(strings)
print("Отсортированные строки:")
print("\n".join(sorted_strings))

