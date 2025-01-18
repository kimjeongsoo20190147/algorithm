n = int(input())
pal_list = []

for _ in range(n):
    pal_list.append(input())

ans = 1

def recursion(s, l, r):
    global ans
    if l >= r: 
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        ans += 1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for element in pal_list:
    print(isPalindrome(element), ans)
    ans = 1