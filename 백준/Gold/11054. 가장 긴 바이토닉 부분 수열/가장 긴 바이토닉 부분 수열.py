N = int(input())
arr = [0] + list(map(int, input().split()))

# solve
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)
dp1[1] = dp2[N] = 1

# dp1
for n in range(2, N + 1):
	dp1[n] = 1
	for i in range(1, n): # dp1[n] 갱신
		if arr[n] > arr[i]:
			dp1[n] = max(dp1[n], dp1[i] + 1)

# dp2
for n in range(N - 1, 0, -1):
	dp2[n] = 1
	for i in range(N, n, -1): # dp2[n] 갱신
		if arr[n] > arr[i]:
			dp2[n] = max(dp2[n], dp2[i] + 1)

ans = 0
for n in range(1, N + 1):
	ans = max(ans, dp1[n] + dp2[n] - 1)

print(ans)