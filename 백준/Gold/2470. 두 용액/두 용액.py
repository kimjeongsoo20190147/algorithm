N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1
min_mix = int(1e12)
ans = [0,0]

while left < right:
    mix_sum = arr[left] + arr[right]
    if abs(mix_sum) < min_mix:
        min_mix = abs(mix_sum)
        ans[0], ans[1] = arr[left], arr[right]

    if mix_sum < 0:
        left += 1
    else:
        right -= 1

ans.sort()

for elem in ans:
    print(elem, end=" ")