a = [6, 5, 12, 4, 2, 7, 8, 10]


def evaluateScores(arr: list, L: int, R: int):
    result = 0
    for i in range(L, R + 1):
        result = result + arr[i]
    return result


# score = evaluateScores([6, 5, 12, 4, 2, 7, 8, 10], 2, 5)
# print(score)

def buildPSArray(arr):
    N = len(arr)
    PS = []
    for i in range(N):
        PS.append(0)

    PS[0] = arr[0]
    for i in range(1, N):
        PS[i] = PS[i - 1] + arr[i]
    print(arr)
    print(PS)
    return PS


def evaluateScores_2(PS: list, L: int, R: int):
    if L == 0:
        return PS[R]
    return PS[R] - PS[L - 1]


PS = buildPSArray(a)
result = evaluateScores_2(PS, 0, 5)
print(result)
