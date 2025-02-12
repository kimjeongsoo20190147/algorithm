n = int(input())

target = 1000 - n
changes = [500,100,50,10,5,1]
ans = 0

for i in changes:
    ans += target // i
    target %= i

print(ans)