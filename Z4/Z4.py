def sort_russian_flag(colors):
    order = {"белый": 0, "синий": 1, "красный": 2}
    return sorted(colors, key=lambda color: order.get(color, 3))


colors = ["красный", "белый", "синий"]
sorted_colors = sort_russian_flag(colors)
print("Упорядоченные цвета флага:", sorted_colors)