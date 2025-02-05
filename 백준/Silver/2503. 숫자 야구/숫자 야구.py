from itertools import permutations

N = int(input())
a = ['1','2','3','4','5','6','7','8','9']
nums = list(permutations(a,3))

for _ in range(N):
    n,s,b = map(int, input().split())
    n = list(str(n))
    cnt = 0
    
    for i in range(len(nums)):
        strike = ball = 0
        i -= cnt
        
        for j in range(3):
            if nums[i][j] == n[j]:
                strike += 1
            elif n[j] in nums[i]:
                ball += 1
             
        if (strike != s) or (ball != b):
            nums.remove(nums[i])
            cnt += 1
            
print(len(nums))