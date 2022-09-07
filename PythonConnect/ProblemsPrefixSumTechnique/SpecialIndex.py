def findSpecialIndex(arr):
    n = len(arr)
    # create PSE and PSO

    PSE = [0 for i in range(n)]
    PSO = [0 for i in range(n)]

    PSE[0] = arr[0]
    PSO[0] = 0

    for i in range(n):
        if i % 2 == 0:
            PSE[i] = PSE[i - 1] + arr[i]
            PSO[i] = PSO[i - 1]
        else:
            PSO[i] = PSO[i - 1] + arr[i]
            PSE[i] = PSE[i - 1]

    SE, SO = 0, 0
    cnt = 0

    for i in range(n):
        if i == 0:
            SE = PSE[0] + PSO[n - 1]
            SO = PSO[0] + PSE[n - 1]
        else:
            SE = PSE[i - 1] + PSO[n - 1] - PSO[i]
            SO = PSO[i - 1] + PSE[n - 1] - PSE[i]
        if SE == SO:
            print(i)
            cnt += 1
    return cnt


print(findSpecialIndex([4, 3, 2, 7, 6, -2]))

# remove 0th element => [3, 2, 7, 6, -2]=> 3 + 7 + -2 == 2 + 6 => 8 == 8
# remove 2nd element => [4, 3, 7, 6, -2] => 4 + 7 + -2 == 3 + 6 => 9 == 9
