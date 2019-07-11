def binary_search_recursive(arr, left, right, x):
    """ Return index of x in arr if present, else -1 """
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:  # If element is smaller than mid, then it can only be present in left subarray
            return binary_search_recursive(arr, left, mid - 1, x)
        elif arr[mid] < x:
            return binary_search_recursive(arr, mid + 1, right, x)
    else:
        return -1


def binary_search_iterative(arr, left, right, x):
    """ Return index of x in arr if present, else -1 """
    while right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    print(*arr)
    result = binary_search_iterative(arr, 0, len(arr) - 1, x)
    print('Element {} is present at index {}'.format(x, result) if result != -1 else 'Element is not present in array')