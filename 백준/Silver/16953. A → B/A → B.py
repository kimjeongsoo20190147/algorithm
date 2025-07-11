x, target = map(int, input().split())
cnt = 0
zero = -1
con = 1

while con:
    if target % 2 == 0:
        target = target // 2
        cnt += 1
    else:
        target = (target -1) / 10
        cnt += 1


    if target == x:
        con = 0
    elif target < x:
        cnt = -2
        con = 0

print(cnt+1)