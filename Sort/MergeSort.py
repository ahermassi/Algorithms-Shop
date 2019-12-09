def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    return merge(left_half, right_half)


def merge(nums1, nums2):
    n, m = len(nums1), len(nums2)
    res = []
    i = j = 0
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i < n:
        res.extend(nums1[i:])
    if j < m:
        res.extend(nums2[j:])
    return res


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print('Array before sorting: ', *arr)
    print('Array after Merge Sort: ', *merge_sort(arr))
