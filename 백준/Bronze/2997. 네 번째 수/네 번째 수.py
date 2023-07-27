numlist = list(map(int, input().split()))
numlist.sort()
d = min(numlist[1]-numlist[0], numlist[2]-numlist[1])
for i in range(len(numlist)):
  temp = numlist[i]
  if temp + d not in numlist:
    print(temp+d)
    break