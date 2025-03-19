n = int(input())

for _ in range(n):
    t = int(input().strip())  # 열(스티커의 칸) 개수

    # 각 행(위, 아래)의 스티커 점수들
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    # dp[i][0] = i번째 열에서 스티커를 선택하지 않았을 때의 최댓값
    # dp[i][1] = i번째 열에서 위 스티커를 선택했을 때의 최댓값
    # dp[i][2] = i번째 열에서 아래 스티커를 선택했을 때의 최댓값
    dp = [[0]*3 for _ in range(t)]

    # 초기값 설정 (0번째 열)
    dp[0][0] = 0             # 0번째 열에서 아무것도 선택 안 함
    dp[0][1] = upper[0]     # 0번째 열에서 위쪽 스티커 선택
    dp[0][2] = lower[0]     # 0번째 열에서 아래쪽 스티커 선택

    if t > 1:
        # 1번째 열 초기값 (점화식 적용)
        dp[1][0] = max(dp[0][0], dp[0][1], dp[0][2])  # 아무 스티커 안 고름
        dp[1][1] = dp[0][2] + upper[1]               # 이전 열에서 아랫줄을 골랐을 때만 윗줄 가능
        dp[1][2] = dp[0][1] + lower[1]               # 이전 열에서 윗줄을 골랐을 때만 아랫줄 가능

        # 2번째 열부터 일반화
        for i in range(2, t):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + upper[i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + lower[i]

    # 마지막 열(t-1)에서의 결과 중 최댓값
    answer = max(dp[t-1][0], dp[t-1][1], dp[t-1][2])
    print(answer)
