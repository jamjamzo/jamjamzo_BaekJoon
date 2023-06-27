l, p = map(int, input().split())
e = list(map(int, input().split()))
n = l*p
e_n = []
for i in e:
  e_n.append((i-n))
print(*e_n,sep=' ')