# 1st Problem
# Given an integer array A of size N and an integer B, you have to print the same array after rotating
# it B times towards the right.
"""a = [1, 2, 3, 4]
b = 2

result = [3, 4, 1, 2]"""


# approach1
def solveRotationGame(arr: list, B: int):
    N = len(arr)  # Store the lenght of the arr
    result = []
    for i in range(N):
        result.append(0)
    B = B % N

    resultIndex = 0

    for i in range(N):
        resultIndex = i + B

        if resultIndex < N:
            result[resultIndex] = arr[i]
        else:
            result[resultIndex % N] = arr[i]

    return result


ans = solveRotationGame([1, 2, 3, 4, 5, 6, 7], 4)
print(ans)


# approach 2 (using reverse approach)
def solveRotationGame2(arr: list, B: int):
    def reverseArray(arr: list, start: int, end: int):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

    N = len(arr)

    reverseArray(arr, 0, N - 1)
    print(arr)
    reverseArray(arr, 0, B - 1)
    print(arr)
    return reverseArray(arr, B, N - 1)


ans = solveRotationGame2([1, 2, 3, 4, 5, 6, 7], 4)
print(ans)
