import sys

def is_lucky(arr):
    """
    리스트 arr(순열)가 인접한 문자가 모두 다른지 검사하는 함수
    """
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
    return True

def next_permutation(a):
    """
    a 리스트의 다음 순열을 in-place로 만듭니다.
    만약 다음 순열이 있다면 True, 더 이상 생성할 순열이 없으면 False를 반환합니다.
    """
    # 1. 뒤에서부터 a[i] < a[i+1]를 만족하는 가장 큰 i를 찾습니다.
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return False  # 마지막 순열입니다.
    
    # 2. a[i]보다 큰 값 중 뒤쪽에서 가장 작은 a[j]를 찾습니다.
    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1
    
    # 3. a[i]와 a[j]를 교환합니다.
    a[i], a[j] = a[j], a[i]
    
    # 4. a[i+1:] 구간을 뒤집습니다.
    a[i+1:] = reversed(a[i+1:])
    return True

# 입력 처리
s = sys.stdin.readline().strip()
# 문자열의 문자들을 정렬합니다. (next_permutation을 위해)
arr = sorted(s)
n = len(arr)
count = 0

# 첫 번째 순열 검사
if is_lucky(arr):
    count += 1

# 다음 순열들을 하나씩 생성하면서 검사
while next_permutation(arr):
    if is_lucky(arr):
        count += 1

print(count)
