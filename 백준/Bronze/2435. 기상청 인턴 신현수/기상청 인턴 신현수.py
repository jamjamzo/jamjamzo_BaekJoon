n, k = map(int, input().split())
t = list(map(int, input().split()))
max_t = -987654321
for i in range(n-k+1):
  hap = 0
  for j in range(k):
    hap += t[i+j]
  max_t = max(hap,max_t)
print(max_t)