N = int(input())
arr1 = set(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    if num in arr1:
        print(1, end=" ")
    else:
        print(0, end=" ")
