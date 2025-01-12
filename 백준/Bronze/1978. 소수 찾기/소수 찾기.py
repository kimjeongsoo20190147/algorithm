n = int(input())
numbers = list(map(int, input().split()))
cnt = 0           

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for num in numbers:
    if is_prime(num):
        cnt += 1

print(cnt)
