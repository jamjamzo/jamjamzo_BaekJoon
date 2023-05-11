n = list(map(int, input().split()))
hap = 0
for i in n:
  hap += i**2
print(hap%10)