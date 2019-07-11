def heap_sort(arr):
    n = len(arr)
    for i in reversed(range(n)):
        heapify(arr, n, i)  # Heapify the tree bottom-up, starting from last element up to the root
    for i in reversed(range(1, n)):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the last element and the root
        heapify(arr, i, 0)  # Heapify the new tree (0 refers to the root == entire tree)


def heapify(arr, n, i):
    """ Heapify the subtree rooted at i, with n size of heap """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:  # If left child exists and is greater than current root
        largest = left
    if right < n and arr[right] > arr[largest]:  # If left child exists and is greater than current largest
        largest = right
    if largest != i:  # If largest changed, then it means there is a new root
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)  # Heapify the subtree rooted at largest (since largest has just been changed)


if __name__ == '__main__':
    arr = [19, 22, 63, 105, 2, 46]
    print('Array before sorting: ', *arr)
    heap_sort(arr)
    print('Array after QuickSort: ', *arr)