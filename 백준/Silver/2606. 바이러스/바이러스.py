from collections import deque

n = int(input())
v = int(input())

visited = [0] * (n+1)

graph = [[] for i in range(n+1)]

for i in range(v):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
visited[1] = 1

q = deque([1])

while q:
    c=q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            q.append(nx)
            visited[nx] = 1
            
print(sum(visited)-1)