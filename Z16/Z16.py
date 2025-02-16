def is_local_minimum(arr, index):
    if not (0 <= index < len(arr)):
        raise ValueError("Индекс выходит за границы массива")

    left = arr[index - 1] if index > 0 else float('inf')
    right = arr[index + 1] if index < len(arr) - 1 else float('inf')

    return arr[index] < left and arr[index] < right


arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
index = int(input("Введите индекс: "))

try:
    result = is_local_minimum(arr, index)
    print("Да" if result else "Нет")
except ValueError as e:
    print("Ошибка:", e)