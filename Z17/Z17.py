def left_shift(arr):
    if not arr:
        return arr
    return arr[1:] + [arr[0]]


arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
shifted_arr = left_shift(arr)

print("Сдвинутый массив:", " ".join(map(str, shifted_arr)))
