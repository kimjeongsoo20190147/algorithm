import sys
input = sys.stdin.read

data = input().split()
idx = 0
T = int(data[idx])
idx += 1

for _ in range(T):
    N = int(data[idx])
    idx += 1
    applicants = []

    for _ in range(N):
        doc, interview = int(data[idx]), int(data[idx + 1])
        applicants.append((doc, interview))
        idx += 2

    # 1. 서류 성적으로 오름차순 정렬
    applicants.sort()

    # 2. 면접 성적 기준 최소값을 유지하며 선발
    count = 1  # 첫 번째 지원자는 무조건 선발
    min_interview = applicants[0][1]

    for i in range(1, N):
        if applicants[i][1] < min_interview:
            count += 1
            min_interview = applicants[i][1]

    print(count)
