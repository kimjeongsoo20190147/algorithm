N = int(input())
input_array = list(map(int, input().split()))
dp = [1] * N  # 최장수열 길이를 저장할 dp 리스트선언

for i in range(N):  # 배열 길이만큼돈다.
    for j in range(i):  # 해당 배열 원소의 직전 원소까지 돈다.
        if input_array[i] > input_array[j]:  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입

print(max(dp))  # 최장길이 출력

subsequence = [] #정답수열 입력할 배열선언
order = max(dp)  # max(dp) 값을 저장
for i in range(N - 1, -1, -1):
    if dp[i] == order:  # 만약 dp[i] 값이 order값과 같다면
        subsequence.append(input_array[i])  # 해당 input_array[i]값을 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

subsequence.reverse()  # 큰수부터 작은수로 뽑았기 때문에
print(*subsequence) #정답수열 출력