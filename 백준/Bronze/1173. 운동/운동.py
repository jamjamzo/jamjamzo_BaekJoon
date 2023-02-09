N, m, M, T, R = map(int, input().split())
cnt = 0
workout = 0
start = m
while workout < N:
  if m + T > M:
    cnt = -1
    break
  cnt += 1
  if start + T <= M:
    start = start + T
    workout += 1
    
  else:
    if start - R < m:
      start = m
    else:
      start = start - R
  
print(cnt)