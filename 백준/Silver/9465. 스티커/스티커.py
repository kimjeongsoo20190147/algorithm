T = int(input())

for _ in range(T):
    n = int(input())

    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    table = []

    table.append(upper)
    table.append(lower)


    dp = [[0] * n for _ in range(2)]

    if n == 1:
        if table[0] > table[1]:
            print(table[0][0])
        else:
            print(table[1][0])
    elif n == 2:
        a = table[0][0] + table[1][1]
        b = table[1][0] + table[0][1]
        if a > b:
            print(a)
        else:
            print(b)
    else:
        dp[0][0] = table[0][0]
        dp[0][1] = table[1][0] + table[0][1]
        dp[1][0] = table[1][0]
        dp[1][1] = table[0][0] + table[1][1]

        ans = []

        for j in range(2,n):
            dp[0][j] = max(dp[1][j-2], dp[1][j-1], dp[0][j-2]) + table[0][j]
            ans.append(dp[0][j])

            dp[1][j] = max(dp[0][j-2], dp[0][j-1], dp[1][j-2]) + table[1][j]
            ans.append(dp[1][j])

        print(max(ans))