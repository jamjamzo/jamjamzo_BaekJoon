n = int(input())
f0 = 0
f1 = 1
for i in range(2,n+1):
  f1 += f0
  f0 = f1 - f0
print(f1)