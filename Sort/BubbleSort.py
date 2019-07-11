def bubble_sort(arr):
    is_sorted = True
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    bubble_sort(arr)
    print('Array after Bubble Sort: ', *arr)