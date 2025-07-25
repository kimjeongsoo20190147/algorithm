# F(총 층), S(강호가 있는 현재 층), G(목표 층), U(위로 몇 층씩 갈 수 있는지), D(아래로 몇 층씩 갈 수 있는지)

from collections import deque


F, S, G, U, D = map(int, input().split())

q = deque()
visited = [False] * (F + 1)
found = False

q.append((0,S))
visited[S] = True

while q:
    push, pos = q.popleft()

    if pos == G:
        print(push)
        found = True
        break

    for next_pos in [pos+U, pos-D]:
        if (1 <= next_pos <= F) and (not visited[next_pos]):
            q.append((push+1, next_pos))
            visited[next_pos] = True

if not found:
    print("use the stairs")