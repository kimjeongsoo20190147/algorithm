import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)

N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append([v,1])


dist = [INF] * (N+1)

pq = PriorityQueue()
dist[X] = 0
pq.put([0,X])

while not pq.empty():
    cur_dist, cur_node = pq.get()
    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist
        if temp_dist < dist[adj_node]:
            dist[adj_node] = temp_dist
            pq.put([temp_dist, adj_node])


index = 0
exist = False

for elem in dist:
    if elem == K:
        print(index)
        exist = True
    index += 1

if not exist:
    print(-1)
