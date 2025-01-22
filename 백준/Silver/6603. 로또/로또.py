from itertools import combinations



while True:
    input_num = list(map(int, input().split()))
    if input_num[0] == 0:
        break
    else:
        input_num = input_num[1:]
        ans = list(combinations(input_num, 6))
        for num in ans:
            for _ in num:
                print(_, end=' ')
            print()
        print()