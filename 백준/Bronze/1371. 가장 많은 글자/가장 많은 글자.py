import sys
input = sys.stdin.read

words = input().replace("\n","").replace(" ","")

aList = [chr(i) for i in range(ord('a'), ord('z')+1)]

aCount = []
for i in range(len(aList)):
  aCount.append(words.count(aList[i]))

aMax = max(aCount)

wordsMax = []
for i in range(len(aCount)):
  if aCount[i] == max(aCount):
    wordsMax.append(aList[i])

wordsMax.sort()
print(*wordsMax,sep='')