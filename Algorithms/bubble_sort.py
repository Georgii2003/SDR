# Алгоритм пузырьковой сортировки

def bubble_sort(arr):
    n = len(arr)

    # Проходим по всему массиву
    for i in range(n):
        # Проверка, были ли выполнены перестановки на текущей итерации
        swapped = False

        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):

            # Следует ли менять местами текущий со следующим
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если на текущей итерации не было выполнено перестановок, значит массив уже отсортирован
        if not swapped:
            break

    return arr

# Пример
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)