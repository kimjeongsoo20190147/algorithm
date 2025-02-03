n = int(input())
li=[]
for _ in range(n):
    a = list(map(int, input().split()))
    li.append(a)

li.sort()

for i in range(n):
    print(li[i][0], end=" ")
    print(li[i][1])