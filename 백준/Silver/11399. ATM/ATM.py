n = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(1,n+1,1):
    ans += sum(A[0:i])
    
print(ans)