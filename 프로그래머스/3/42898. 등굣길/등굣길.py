def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for x in range(m):
        for y in range(n):
            if [x+1,y+1] in puddles:
                dp[x][y] = 0
                continue
            if x == 0 and y == 0:
                continue
            if y > 0:
                left = dp[x][y-1]
            else:
                left = 0
                
            if  x > 0:
                up = dp[x-1][y]
            else:
                up = 0
                
            dp[x][y] = (left+up) % 1000000007

    return dp[m-1][n-1]