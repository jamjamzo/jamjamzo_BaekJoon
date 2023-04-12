import sys
input = sys.stdin.readline
n = int(input())
nlist = set(map(int,input().split()))
m = int(input())
mlist = list(map(int, input().split()))

for i in range(m):
  if mlist[i] in nlist:
    print(1, end=' ')
  else:
    print(0, end=' ')