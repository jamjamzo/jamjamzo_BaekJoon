import sys
input = sys.stdin.readline
n,m = map(int, input().split())
s = set()
for _ in range(n):
  s.add(input())
cnt = 0
for _ in range(m):
  c = input()
  if c in s:
    cnt += 1

print(cnt)