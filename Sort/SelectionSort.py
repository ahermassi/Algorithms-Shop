def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        # Find the index of min element
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


def selection_sort_recursive(nums, start):
    n = len(nums)
    if start == n - 1:
        return
    min = start
    for i in range(start + 1, n):
        if nums[i] < nums[min]:
            min = i
    nums[start], nums[min] = nums[min], nums[start]
    selection_sort_recursive(nums, start + 1)


if __name__ == '__main__':
    nums = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *nums)
    selection_sort(nums)
    print('Array after Selection Sort: ', *nums)

    nums = [64, 25, 12, 22, 11]
    print('Array before recursive sorting: ', *nums)
    selection_sort_recursive(nums, 0)
    print('Array after recursive Selection Sort: ', *nums)

