N, K = map(int, input().split())

cnt = 0
remove_list = [False] * (N+1)

for i in range(2, N+1):
    if not remove_list[i]:
        remove_list[i] = True
        cnt += 1
        if cnt == K:
            print(i)
        for mul_num in range(i, N+1, i):
            if not remove_list[mul_num]:
                remove_list[mul_num] = True
                cnt += 1
                if cnt == K:
                    print(mul_num)