import sys
n = int(input())
ans = [-1] * n
A = list(map(int, sys.stdin.readline().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)
    
    

    
print(*ans)