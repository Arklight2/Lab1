from collections import Counter

def build_L1_L2(arr):
    counts = Counter(arr)
    L1 = list(counts.keys())
    L2 = list(counts.values())
    return L1, L2


arr = list(map(int, input("Введите элементы списка через пробел: ").split()))
L1, L2 = build_L1_L2(arr)

print("L1:", " ".join(map(str, L1)))
print("L2:", " ".join(map(str, L2)))
