T = int(input().strip())
    
# 2. 10,000 이하 모든 수에 대해 소수 여부를 미리 구해둔다 (에라토스테네스의 체)
max_limit = 10000
sieve = [True] * (max_limit + 1)
sieve[0], sieve[1] = False, False  # 0, 1은 소수가 아님
    
for i in range(2, int(max_limit**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, max_limit + 1, i):
            sieve[j] = False
    
# 3. 테스트 케이스 T번 반복
for _ in range(T):
    n = int(input().strip())  # 짝수 n
        
    # 골드바흐 파티션 찾기
    # -- n//2에서 시작해서 좌우로 이동하면 두 소수의 차이가 최소인 경우를 가장 먼저 찾을 수 있음
    left = n // 2
    right = n // 2
        
    while True:
        if sieve[left] and sieve[right]:  # 둘 다 소수
            if left + right == n:
                print(left, right)
                break
        left -= 1
        right += 1