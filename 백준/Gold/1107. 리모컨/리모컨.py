N = int(input())
M = int(input())

broken = set()

if M > 0:
    broken = set(map(int, input().split()))
    
answer = abs(N-100)

for x in range(1000001):
    x_str = str(x)
    
    possible = True
    
    for ch in x_str:
        if int(ch) in broken:
            possible = False
            break
            
    if possible:
        press_count = len(x_str) + abs(N-x)
        answer = min(answer, press_count)
        
print(answer)
