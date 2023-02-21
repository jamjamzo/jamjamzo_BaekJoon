a,b = map(int, input().split())
c = []
for i in range(1, b+1):
  for j in range(i):
    c.append(i)

print(sum(c[a-1:b]))