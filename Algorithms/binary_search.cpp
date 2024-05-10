// Алгоритм бинарного поиска

#include <iostream>
using namespace std;

int binarySearch(int arr[], int left, int right, int x) {
    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Если x находится в середине
        if (arr[mid] == x)
            return mid;

        // Если x больше, игнорируем левую половину
        if (arr[mid] < x)
            left = mid + 1;

        // Если x меньше, игнорируем правую половину
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {2, 3, 4, 10, 40, 50, 80, 93, 100};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    if (result == -1)
        cout << "Элемент не найден в массиве";
    else
        cout << "Элемент найден в индексе: " << result;
    return 0;
}