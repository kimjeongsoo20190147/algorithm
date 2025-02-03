n = int(input())

score = [list(map(int, input().split())) for _ in range(n)]

score = sorted(score, key=lambda x:(x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for i in score[:3]:
    print(i[0], end=" ")