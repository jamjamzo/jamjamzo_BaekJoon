import sys
input = sys.stdin.readline
n = int(input())
main = 1
cnt = 0
for i in range(n):
  a = int(input())
  if a > main:
    cnt += (a-1)
  elif a == main:
    cnt += 0

if cnt == 0:
  print(1)
else:
  print(cnt+1)
    