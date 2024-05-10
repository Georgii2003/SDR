#Алгоритм бинарного поиска

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Если искомый элемент найден, возвращаем его индекс
        if arr[mid] == target:
            return mid
        # Если искомый элемент меньше среднего, ищем в левой половине
        elif arr[mid] > target:
            high = mid - 1
        # Иначе ищем в правой половине
        else:
            low = mid + 1

    # Если элемент не найден, возвращаем -1
    return -1

# Пример
sorted_list = [2, 3, 4, 10, 40]
target_element = 10
result = binary_search(sorted_list, target_element)

if result != -1:
    print("Элемент найден в индексе", result)
else:
    print("Элемент не найден в массиве")