target = int(input())

ans = 0

while target >= 0:
    if target % 5 ==0:
        ans += (target // 5)
        print(ans)
        break
    target -= 3
    ans += 1

else:
    print(-1)