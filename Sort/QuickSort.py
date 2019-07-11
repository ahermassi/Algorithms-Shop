def quick_sort(arr, left, right):
    """ Parallel QuickSort """
    if len(arr) == 0 or len(arr) == 1:
        return
    pivot = right
    right -= 1
    while left <= right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    temp = arr[pivot]
    arr[left], arr[pivot] = arr[pivot], arr[left]
    left_arr = arr[:left]
    right_arr = arr[left + 1:]
    quick_sort(left_arr, 0, len(left_arr) - 1)
    quick_sort(right_arr, 0, len(right_arr) - 1)
    arr.clear()
    arr += left_arr + [temp] + right_arr


if __name__ == '__main__':
    arr = [19, 22, 63, 105, 2, 46]
    print('Array before sorting: ', *arr)
    quick_sort(arr, 0, len(arr) - 1)
    print('Array after QuickSort: ', *arr)
