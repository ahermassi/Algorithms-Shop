def quicksort(nums, left, right):
    """ This version picks the last item in the partition space as the pivot every time, but there are many other ways
    to choose a pivot item. """

    if left < right:
        # Partition the array from left to right and find where the selected pivot belongs
        pivot = partition(nums, left, right)
        quicksort(nums, left, pivot - 1)
        quicksort(nums, pivot + 1, right)


def partition(nums, left, right):
    """ The partition function that chooses a pivot, partitions the array around the pivot, places the pivot value
        where it belongs, and then returns the index of where the pivot finally lies.
        The invariant of this algorithm is:
            All elements up to and including index i are less than the pivot.
            All elements between i and j are greater than the pivot.
            All elements between j and right are unclassified (yet).
    """

    pivot = nums[right]  # In this implementation of quicksort, we pick the last item in the partition space as the
    # pivot every time. This can turn out very good or very bad,
    i = left - 1  # i will keep track of the 'tail' of the section of items less than the pivot so that at the end we
    # can 'sandwich' the pivot between the section less than it and the section greater than it.
    j = left  # j will scan for us
    while j < right:
        if nums[j] <= pivot:  # If this item is less than the pivot, it needs to be moved to the section of items
            # less than the pivot
            i += 1  # Move i forward so that we can swap the value at j into the tail of the items less than the pivot
            nums[i], nums[j] = nums[j], nums[i]  # Execute the swap
        j += 1
    nums[i + 1], nums[right] = nums[right], nums[i + 1]  # Swap the pivot value right after the section of items less
    # than the pivot. i keeps the tail of this section
    return i + 1  # Return the pivot's final resting position


if __name__ == '__main__':
    nums = [19, 22, 63, 105, 2, 46]
    print('Array before sorting: ', *nums)
    quicksort(nums, 0, len(nums) - 1)
    print('Array after QuickSort: ', *nums)
