import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)

def dijkstra(start_node):
    global N, adj_list
    
    dist = [INF] * (N+1)
    
    pq = PriorityQueue()
    dist[start_node] = 0
    pq.put([0,start_node])
    
    while not pq.empty():
        cur_dist, cur_node = pq.get()
        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                pq.put([temp_dist, adj_node])
                
    return dist


N, M, X = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,t = map(int, input().split())
    adj_list[a].append([b,t])
    
    
dist = [None] * (N+1)
for i in range(1, N+1):
    dist[i] = dijkstra(i)
    
    
ans = -1

for i in range(1, N+1):
    ans = max(ans, dist[i][X]+dist[X][i])
    
print(ans)