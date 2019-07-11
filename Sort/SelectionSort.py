def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        # Find the index of min element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def selection_sort_recursive(arr, start):
    if start == len(arr) - 1:
        return
    min = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[start], arr[min] = arr[min], arr[start]
    selection_sort_recursive(arr, start + 1)


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    selection_sort(arr)
    print('Array after Selection Sort: ', *arr)

    arr = [64, 25, 12, 22, 11]
    print('Array before recursive sorting: ', *arr)
    selection_sort_recursive(arr, 0)
    print('Array after recursive Selection Sort: ', *arr)

