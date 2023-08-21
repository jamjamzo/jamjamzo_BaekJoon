t = int(input())
for _ in range(t):
  a,b = input().split()
  c = str(int(a[::-1]) + int(b[::-1]))
  print(int(c[::-1]))