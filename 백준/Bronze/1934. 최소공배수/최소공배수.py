# 방법 2
t = int(input())
for i in range(t):
  a,b = map(int, input().split())
  x, y = a, b

  while a%b != 0:
    a,b = b, a%b
  print(x*y//b)