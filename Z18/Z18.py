def split_even_odd_indices(arr):
    even_index_elements = [arr[i] for i in range(0, len(arr), 2)]
    odd_index_elements = [arr[i] for i in range(1, len(arr), 2)]
    return even_index_elements + odd_index_elements

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
result = split_even_odd_indices(arr)

print("Результат:", " ".join(map(str, result)))
