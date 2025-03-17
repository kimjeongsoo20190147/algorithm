n, m = map(int, input().split())
li = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + li[i-1]

ans = 0
ans_li = []
for i in range(m):
    a,b = map(int, input().split())
    ans = dp[b] - dp[a-1]
    ans_li.append(ans)


for elem in ans_li:
    print(elem)