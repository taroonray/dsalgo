"""
Q1. Equilibrium Index of an Array. Given an Array of size N, find the number of equilibrium indices present in that array. An index "i" can be called "equilibrium" if sum of all the elements to the left of "i" is equal to the sum of elements to the right of "i".
If no such index is found, then return "-1"


For example:
A=[-7, 1, 5, 2, -4, 3, 0]
Output-> 1
Explanation:
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]


A=[1,2,3]
Output -> -1
Explanation:
No index is qualified to be equilibrium

"""


# Brute Foce (TC - N^2 | SC - 1)
def findEquilibriumIndex(arr):
    cnt = 0
    n = len(arr)

    for i in range(n):
        if i not in (0, n - 1):
            sl = 0
            for j in range(i):
                sl = sl + arr[j]
            sr = 0
            for k in range(i + 1, n):
                sr = sr + arr[k]
            if sl == sr:
                cnt += 1
    return cnt


print(findEquilibriumIndex([-7, 1, 5, 2, -4, 3, 0]))


# Optimization (TC - N | SC - N)
def findEquilibriumIndex2(arr):
    n = len(arr)
    cnt = 0
    leftArr = [0 for i in range(n)]
    rightArr = [0 for i in range(n)]

    leftArr[0] = 0
    rightArr[n - 1] = 0

    for i in range(1, n):
        leftArr[i] = leftArr[i - 1] + arr[i - 1]

    for j in range(n - 2, -1, -1):
        rightArr[j] = rightArr[j + 1] + arr[j + 1]

    for k in range(n):
        if leftArr[k] == rightArr[k] and k not in (0, n - 1):
            cnt += 1

    return cnt


print(findEquilibriumIndex2([-7, 1, 5, 2, -4, 3, 0]))


# Optimization 2
def findEquilibriumIndex3(arr):
    n = len(arr)
    PS = [0 for i in range(n)]
    cnt = 0
    for i in range(n):
        PS[i] = PS[i - 1] + arr[i]

    for i in range(1, n - 1):
        ls, rs = 0, 0
        if i == 0:
            ls = 0
        else:
            ls = ls + PS[i - 1]

        rs = PS[n - 1] - PS[i]
        if ls == rs:
            cnt += 1
    return cnt


print(findEquilibriumIndex3([-7, 1, 5, 2, -4, 3, 0]))
