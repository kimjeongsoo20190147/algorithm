S = int(input())
N = 0
cnt = 0
while True:
    if S > N:
        N += 1
        S = S - N
        cnt += 1
    else:
        print(cnt)
        break