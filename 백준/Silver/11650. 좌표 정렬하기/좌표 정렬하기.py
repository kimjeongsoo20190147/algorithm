n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

lst = sorted(lst)

for _ in lst:
    for elem in _:
        print(elem, end=" ")
    print()