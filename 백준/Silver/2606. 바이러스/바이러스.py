# DFS풀이

def dfs(node):
    # 인접리스트, 방문기록, 감염된 컴퓨터 수
    global adj_list, visited, cnt
    
    # base case
    if visited[node]:
        return
    visited[node] = 1
    
    cnt += 1
    
    # recursive case
    for adj_node in adj_list[node]:
        dfs(adj_node)
        
# 노드 수(컴퓨터 수)
N = int(input())
# 간선 수(연결된 컴퓨터 수)
M = int(input())

# 빈 인접리스트 초기화
adj_list = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 방향이 없는 그래프이므로 반대 경우도 인접리스트에 append
    adj_list[a].append(b)
    adj_list[b].append(a)
    
# 방문한 적 있는지 기록하는 리스트 초기화
visited = [False] * (N+1)

cnt = 0
dfs(1)

print(cnt-1)