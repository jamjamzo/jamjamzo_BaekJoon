total = 0
max_t = 0
for i in range(10):
  a,b = map(int, input().split())
  total = total + b - a
  max_t = max(max_t,total)

print(max_t)
