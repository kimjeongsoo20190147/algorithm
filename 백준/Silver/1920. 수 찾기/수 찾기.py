N = int(input())
arr = set(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(1 if num in arr else 0)