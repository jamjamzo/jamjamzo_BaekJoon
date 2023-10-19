n = int(input())
info = []
for _ in range(n):
  w, h = map(int, input().split())
  info.append((w,h))

rank = []
for i in range(n):
  count = 0
  for j in range(n):
    if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
      count += 1
  rank.append(count + 1)

for i in rank:
  print(i, end=" ")
