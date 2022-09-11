def findSubarrayWithLargestSum(arr):
    n = len(arr)
    largest = float('-inf')
    si, sj = -1, -1
    for i in range(n):
        for j in range(i, n):
            _sum = 0
            for k in range(i, j + 1):
                _sum = _sum + arr[k]
            if _sum > largest:
                si, sj = i, j
                largest = _sum
    _slice = slice(si, sj + 1)
    print(arr[_slice])
    return largest


arr = [-7, 2, 3, -8, 4, -10]
print(findSubarrayWithLargestSum(arr))


def findSubarrayWithLargestSum2(arr: list):
    "finding the max sum possible among all the subarrays"
    n = len(arr)
    largest = float('-inf')
    # build PS
    PS = [0 for i in range(n)]
    PS[0] = arr[0]
    for i in range(n):
        PS[i] = PS[i - 1] + arr[i]
    print(PS)
    for i in range(n):
        _sum = 0
        for j in range(i, n):
            if i == 0:
                _sum = PS[0]
            else:
                _sum = PS[j] - PS[i-1]

            if _sum > largest:
                largest = _sum
    return largest

print(findSubarrayWithLargestSum2(arr))


def findSubArraysWithLargestSumKadane(arr):
    n = len(arr)
    largest = float('-inf')
    _sum = 0
    for i in range(n):
        _sum = _sum + arr[i]
        if _sum < 0:
            _sum = 0
        if _sum > largest:
            largest = _sum
    return largest


print(findSubArraysWithLargestSumKadane([1, 3, -5, 6, -4, 2, 7, -2, -5, 4]))