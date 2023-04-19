import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nCnt = {}
for i in nlist:
  if i in nCnt:
    nCnt[i] += 1
  else:
    nCnt[i] = 1

for j in mlist:
  a = nCnt.get(j)
  if a == None:
    print(0, end=" ")
  else:
    print(a, end=" ")