p,m = map(int, input().split())
if p-m <0 or (p-m)%2 != 0:
  print(-1)
else:
  p2 = (p+m) // 2
  q = (p-p2)

  print(max(p2,q), min(p2,q))