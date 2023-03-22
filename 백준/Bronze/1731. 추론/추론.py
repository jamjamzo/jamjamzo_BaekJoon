n = int(input())
nList = [int(input()) for i in range(n)]

if nList[2]-nList[1] == nList[1]-nList[0]:
  q = nList[1] - nList[0]
  print(nList[n-1] + q)

elif nList[2]//nList[1] == nList[1]//nList[0]:
  q = nList[1]//nList[0]
  print(nList[n-1]*q)