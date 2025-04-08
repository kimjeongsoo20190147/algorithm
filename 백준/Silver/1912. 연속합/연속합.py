n = int(input())
A = list(map(int,input().split()))

dp = [0] * n
dp[0] = A[0]


for i in range(1,n):
    dp[i] = max(A[i],A[i]+dp[i-1])

    
print(max(dp))