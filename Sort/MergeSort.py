def merge_sort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    # After the mergeSort functions above finish executing, merge the sorted left array and right array together
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    merge_sort(arr)
    print('Array after Merge Sort: ', *arr)
