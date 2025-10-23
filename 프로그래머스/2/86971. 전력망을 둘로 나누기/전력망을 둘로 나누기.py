from collections import deque


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count
                


def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n+1)
        count = bfs(v1, graph, visited)
        
        diff = abs(count - (n-count))
        answer = min(answer, diff)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer