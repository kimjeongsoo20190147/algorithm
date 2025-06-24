def cantor(n):
    if n == 0:
        print("-", end="")
        return
    else:
        cantor(n-1)
        print(" " * (3 ** (n-1)), end="")
        cantor(n-1)


while True:
    try:
        n = int(input())
        cantor(n)
        print()
    except:
        break