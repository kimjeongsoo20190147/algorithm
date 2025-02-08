from itertools import combinations

a,b = map(int, input().split())
li = list(map(int, input().split()))

com_list = [list(c) for c in combinations(li, 3)]
com_sum = 0
ans_list = []


for i in range(len(com_list)):
    com_sum = sum(com_list[i])
    if com_sum <= b:
        ans_list.append(com_sum)

print(max(ans_list))