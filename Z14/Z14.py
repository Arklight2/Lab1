from collections import Counter
import string


def most_common_global_char(strings):
    total_counts = Counter("".join(strings).lower())
    return total_counts.most_common(1)[0][0] if total_counts else None


def quadratic_deviation_from_global(s, global_char):
    if not global_char:
        return float('inf')

    s = s.lower()
    char_counts = Counter(s)
    total_chars = sum(char_counts.values())

    if total_chars == 0:
        return float('inf')

    global_freq = char_counts[global_char] / total_chars
    expected_freq = 1 / len(string.ascii_lowercase)
    return (global_freq - expected_freq) ** 2


def sort_strings_by_global_char_deviation(strings):
    global_char = most_common_global_char(strings)
    return sorted(strings, key=lambda s: quadratic_deviation_from_global(s, global_char))



n = int(input("Введите количество строк: "))
strings = [input(f"Введите строку {i + 1}: ") for i in range(n)]

sorted_strings = sort_strings_by_global_char_deviation(strings)
print("Отсортированные строки:")
print("\n".join(sorted_strings))
