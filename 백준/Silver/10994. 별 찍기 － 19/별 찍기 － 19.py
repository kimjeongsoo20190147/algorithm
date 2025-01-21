n=int(input())
m=4*n-3
a=[[' ']*m for _ in range(m)]
def r(i):
    if i==m+1:return
    for j in range(i,m-i): a[i][j],a[m-i-1][j]='*','*'
    for j in range(i,m-i): a[j][i],a[j][m-i-1]='*','*'
    r(i+2)
r(0)
for i in a:print(*i,sep='')