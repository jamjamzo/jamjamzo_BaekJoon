# 방법2
short = [int(input()) for _ in range(9)]
sum9 = sum(short)
a = 0
b = 0
for i in range(8):
  for j in range(i+1, 9):
    if sum9 - (short[i] + short[j]) == 100:
      a = short[i]
      b = short[j]

short.remove(a)
short.remove(b)
print(*sorted(short), sep='\n')