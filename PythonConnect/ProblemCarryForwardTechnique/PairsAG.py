def findPairsAG(arr):
    n = len(arr)
    cnt = 0
    countArray = [0 for i in range(n)]
    ans = 0

    for i in range(n - 1, -1, -1):
        if arr[i] == 'g':
            cnt += 1
            countArray[i] = cnt
        else:
            countArray[i] = cnt
    print(countArray)

    for i in range(n):
        if arr[i] == 'a':
            ans += countArray[i]
    return ans


print(findPairsAG(['b', 'a', 'a', 'g', 'a', 'g', 'a', 'g']))


def findPairsAG2(arr):
    cnt, ans = 0, 0
    n = len(arr)

    for i in range(n-1, -1, -1):
        if arr[i] == 'g':
            cnt += 1
        elif arr[i] == 'a':
            ans = ans + cnt
    return ans


print(findPairsAG2(['b', 'a', 'a', 'g', 'a', 'g', 'a', 'g']))
