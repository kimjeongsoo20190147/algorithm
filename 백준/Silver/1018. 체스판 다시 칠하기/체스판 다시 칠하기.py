n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
ans = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = cnt2 = 0
        # 8×8 부분 보드를 순회합니다.
        for x in range(8):
            for y in range(8):
                # (x+y)가 짝수인 칸은 top-left 색과 같아야 함
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':  # top-left가 'W'인 경우
                        cnt1 += 1
                    if board[i + x][j + y] != 'B':  # top-left가 'B'인 경우
                        cnt2 += 1
                else:
                    if board[i + x][j + y] != 'B':  # top-left가 'W'인 경우
                        cnt1 += 1
                    if board[i + x][j + y] != 'W':  # top-left가 'B'인 경우
                        cnt2 += 1
        ans = min(ans, cnt1, cnt2)

print(ans)
