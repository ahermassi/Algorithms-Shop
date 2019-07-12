def radix_sort(arr):
    radix = len(str(max(arr)))
    leading_zeroes = []
    for i in range(len(arr)):
        leading_zeroes.append(str(arr[i]).zfill(radix))
    print('Array after adding leading zeroes: ', leading_zeroes)
    for i in range(radix):
        digits = []
        for s in leading_zeroes:
            digit = s[radix - i - 1]
            digits.append(int(digit))
        print('Iteration {}. Digits to sort: {}'.format(i + 1, digits))
        max_val = max(digits)
        leading_zeroes = count_sort(leading_zeroes, 0, max_val, radix - i - 1)
        print('After iteration {} the array is {}'.format(i + 1, leading_zeroes))
    return [int(i) for i in leading_zeroes]


def count_sort(arr, min_val, max_val, pos):
    counter = [0] * (max_val - min_val + 1)
    for i in range(len(arr)):
        temp = arr[i]
        counter[int(temp[pos])] += 1
    print('Counter: ', counter)
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    for i in reversed(range(1, len(counter))):
        counter[i] = counter[i - 1]
    counter[0] = 0
    result = [None] * len(arr)
    for i in range(len(arr)):
        temp = counter[int(arr[i][pos])]
        result[temp] = arr[i]
        counter[int(arr[i][pos])] += 1
    return result


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]    # [9,4,1,7,9,1,2,0]
    print('Array before sorting: ', *arr)
    result = radix_sort(arr)
    print('Array after Radix Sort: ', *result)