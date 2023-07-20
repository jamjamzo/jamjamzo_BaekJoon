bar = list(map(int, input().split()))
bar_len = len(bar)

for i in range(bar_len-1):
  for j in range(bar_len-1):
    if bar[j] > bar[j+1]:
      bar[j], bar[j+1] = bar[j+1], bar[j]
print(bar[0] * bar[-2])