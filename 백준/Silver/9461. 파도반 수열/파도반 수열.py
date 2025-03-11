T = int(input())

ans_li = []

for i in range(T):
    ans_num = int(input())
    ans_li.append(ans_num)


dp = [0] * max(ans_li)
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4

n = max(ans_li)

for i in range(7, n):
    dp[i] = dp[i-1] + dp[i-5]


for ele in ans_li:
    print(dp[ele-1])
