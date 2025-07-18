N = int(input())

dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2

for i in range(3, N):
    dp[i] = dp[i-1] + dp[i-2]


if N == 1:
    print(1)
else:
    print(dp[N-1])

