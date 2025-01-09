import math

N = int(input())
# 백색이 위로 오게 되는 깃발(= 완전제곱수)의 개수
answer = int(math.isqrt(N))
print(answer)