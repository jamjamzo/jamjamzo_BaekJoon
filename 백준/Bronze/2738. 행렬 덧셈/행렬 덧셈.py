n,m = map(int, input().split())

a = []
for i in range(n):
  aa = list(map(int,input().split()))
  a.append(aa)

b = []
for i in range(n):
  bb = list(map(int,input().split()))
  b.append(bb)

for i in range(n):
  for j in range(m):
    print(a[i][j] + b[i][j], end = ' ')
  print()
