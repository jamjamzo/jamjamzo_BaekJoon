n = int(input())
stairs = list(map(int, input().split()))
a = 0
b = []
for i in range(n-1):
  if stairs[i] < stairs[i+1]:
    a += (stairs[i+1] - stairs[i])
  else:
    b.append(a)
    a = 0
b.append(a)
print(max(b))