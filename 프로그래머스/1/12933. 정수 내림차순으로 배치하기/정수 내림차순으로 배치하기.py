def solution(n):
    answer = 0
    A = [int(digit) for digit in str(n)]
    A.sort(reverse=True)
    answer = int("".join(map(str,A)))
    return answer