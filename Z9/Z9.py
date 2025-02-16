def sort_strings_by_length(strings):
    return sorted(strings, key=len)


n = int(input("Введите количество строк: "))
strings = [input(f"Введите строку {i+1}: ") for i in range(n)]

sorted_strings = sort_strings_by_length(strings)
print("Отсортированные по длине строки:")
print("\n".join(sorted_strings))