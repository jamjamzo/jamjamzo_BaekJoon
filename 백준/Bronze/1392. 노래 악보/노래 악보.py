import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nList = []
for i in range(n):
  second = int(input())
  for j in range(second):
    nList.append(i+1)
qList = [int(input()) for _ in range(q)]
for k in qList:
  print(nList[k])


  