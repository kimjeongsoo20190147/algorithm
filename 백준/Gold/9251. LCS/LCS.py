X = input()
Y = input()

n,m = len(X), len(Y)

dp = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

# 인덱스 에러를 피하기 위해 X와 Y의 맨 앞에 아무 문자나 추가
X, Y = '#'+X, '#'+Y

def LCS(X,Y):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


print(LCS(X,Y))