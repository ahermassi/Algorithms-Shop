def count_sort(arr, min_val, max_val):
    counter = [0] * (max_val - min_val + 1)
    for i in range(len(arr)):
        counter[arr[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    for i in reversed(range(1, len(counter))):
        counter[i] = counter[i - 1]
    counter[0] = 0
    result = [None] * len(arr)
    for i in range(len(arr)):
        temp = counter[arr[i]]
        result[temp] = arr[i]
        counter[arr[i]] += 1
    return result


if __name__ == '__main__':
    arr = [19, 22, 63, 105, 2, 46]  # [9,4,1,7,9,1,2,0]
    print('Array before sorting: ', *arr)
    result = count_sort(arr, 0, 105)
    print('Array after Counting Sort: ', *result)