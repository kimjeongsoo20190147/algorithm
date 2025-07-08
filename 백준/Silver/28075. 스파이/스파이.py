n,m = map(int, input().split())
mission = [list(map(int, input().split())) for i in range(2)]


def spy(day, last_place, total):
    if day == n:
        if total >= m:
            return 1
        else:
            return 0

    count = 0
    for task in range(2):
        for place in range(3):
            score = mission[task][place]
            if place == last_place:
                score //= 2
            count += spy(day+1, place, total+score)
    return count

print(spy(0,-1,0))