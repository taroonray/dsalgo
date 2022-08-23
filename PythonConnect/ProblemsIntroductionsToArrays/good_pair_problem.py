"""
given an integer array A of size N with only unique elements and integer B, find a pair (a[i], a[j]) such that i != j
and a[i] +  a[j] = B
if such a pair exists, then say "yes", if no such pair exists then return "no"

a = [1, 2, 3, 4]
b = 7
Output = yes

a = [1, 2, 4]
b = 4
Output = no
"""


def doesGoodPairExist(arr: list, b: int):
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if arr[i] + arr[j] == b:
                return "yes"
    return "no"


print(doesGoodPairExist([1, 2, 3, 4], 7))


def doesGoodPairExist2(arr: list, b: int):
    N = len(arr)
    i = 0
    j = N - 1
    while i < j:
        if arr[i] + arr[j] == b:
            return "yes"
        elif arr[i] + arr[j] < b:
            i += 1
        else:
            j -= 1
    return "no"


print(doesGoodPairExist2([1, 2, 3, 4], 8))
