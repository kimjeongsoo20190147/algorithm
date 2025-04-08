import sys
input = lambda: sys.stdin.readline().rstrip()

# input
N = int(input())

times = []
for _ in range(N):
	s, e = map(int, input().split())
	times.append((s, e))

# solve
times = sorted(times, key=lambda x : (x[1], x[0]))

ans = 0
end = 0
for s, e in times:
	if s >= end:
		ans += 1
		end = e

print(ans)