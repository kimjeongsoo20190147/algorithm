import sys

def round_half_up(mean):
    # 문제 요구: 소수점 첫째 자리에서 반올림 (음수도 올바르게 처리)
    return int(mean + 0.5) if mean >= 0 else int(mean - 0.5)

def main():
    input = sys.stdin.readline

    n = int(input())
    OFFSET = 4000
    freq = [0] * 8001

    s = 0
    mn = 4001
    mx = -4001

    for _ in range(n):
        v = int(input())
        s += v
        if v < mn:
            mn = v
        if v > mx:
            mx = v
        freq[v + OFFSET] += 1

    # 1) 산술평균
    print(round_half_up(s / n))

    # 2) 중앙값: (n은 홀수) -> (n//2)+1번째 수
    target = n // 2 + 1
    acc = 0
    median = 0
    for i in range(8001):
        acc += freq[i]
        if acc >= target:
            median = i - OFFSET
            break
    print(median)

    # 3) 최빈값: 여러 개면 두 번째로 작은 값
    max_freq = 0
    for f in freq:
        if f > max_freq:
            max_freq = f

    mode = 0
    found_first = False
    for i in range(8001):
        if freq[i] == max_freq:
            if not found_first:
                mode = i - OFFSET
                found_first = True
            else:
                mode = i - OFFSET
                break
    print(mode)

    # 4) 범위
    print(mx - mn)

if __name__ == "__main__":
    main()
