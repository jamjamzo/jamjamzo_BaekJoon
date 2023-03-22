# 방법4
n,c = map(int,input().split())
a = [0] * (c+1)
for _ in range(n):
  f = int(input())
  if f == 1:
    print(c)
    quit()

  for i in range(f,c+1,f):
    a[i] = 1
print(sum(a))