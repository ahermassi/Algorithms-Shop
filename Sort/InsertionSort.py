def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i -1  # Start looking to your left elements
        while j >= 0 and arr[j] > temp:  # While the are elements to the left that are greater than the current one
            arr[j + 1] = arr[j]  # Slide to the right
            j -= 1  # One more step backwards
        arr[j + 1] = temp


def insertion_sort_v1(arr):
    for i in range(len(arr)):
        min = i
        # Find the index of min element -- Same as selection sort
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        # Slide to the right
        temp = arr[min]  # Save the min element to place later
        for k in reversed(range(i + 1, min + 1)):
            # Slide everything from current element until min
            # If list = [5, 12, 11, 13, 6], current index = 1, then min = 4 -> temp = list[min] = 6,
            # slide -> [5, None, 12, 11, 13] -> place temp in second place: [5, 6, 12, 11, 13]
            arr[k] = arr[k - 1]
        arr[i] = temp


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    insertion_sort(arr)
    print('Array after Insertion Sort: ', *arr)

    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    insertion_sort_v1(arr)
    print('Array after Insertion Sort (v1): ', *arr)
