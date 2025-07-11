n = int(input())

km = list(map(int, input().split()))
price = list(map(int, input().split()))

total_cost = 0
i = 0

while i < n-1:
    distance = 0
    current_price = price[i]

    for j in range(i, n-1):
        distance += km[j]
        if price[j+1] < current_price:
            break
    total_cost += distance * current_price
    i = j+1


print(total_cost)