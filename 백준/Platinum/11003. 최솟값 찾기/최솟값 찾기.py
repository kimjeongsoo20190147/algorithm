from collections import deque
import sys
imput = sys.stdin.readline


N,L = map(int, input().split())
mydeque = deque()
temp = list(map(int, input().split()))

for i in range(N):
	while mydeque and mydeque[-1][0] > temp[i]:
		mydeque.pop()
	mydeque.append((temp[i], i))
	if mydeque[0][1] <= i-L:
		mydeque.popleft()
	print(mydeque[0][0], end=" ")