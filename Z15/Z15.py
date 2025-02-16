def is_global_maximum(arr, index):
    if not (0 <= index < len(arr)):
        raise ValueError("Индекс выходит за границы массива")

    return arr[index] == max(arr)



arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
index = int(input("Введите индекс: "))

try:
    result = is_global_maximum(arr, index)
    print("Да" if result else "Нет")
except ValueError as e:
    print("Ошибка:", e)
