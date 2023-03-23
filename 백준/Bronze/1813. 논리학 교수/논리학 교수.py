n = int(input())
board = [0]*51 # 1<=n<=50
true = []
nList = list(map(int, input().split()))

for i in range(n):
  board[nList[i]] += 1


for j in range(len(board)):
  if j == board[j]:
    true.append(j)

if true == []:
  print(-1)
else:
  print(max(true))