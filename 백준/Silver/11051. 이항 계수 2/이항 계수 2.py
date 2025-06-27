n, k = map(int, input().split())

dp = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(0, n+1):
    dp[i][1] = i
    dp[i][0] = 1
    dp[i][i] = 1
    

for i in range(2,n+1):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][j] = dp[i][j] % 10007
        
        
print(dp[n][k])