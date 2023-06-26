a,b = input().split()
n = len(a)
m = len(b)
board = [['.']*n for _ in range(m)]

row = 0
col = 0
for i in range(n):
  if a[i] in b:
    row = i
    col = b.index(a[i])
    break

for i in range(m):
  board[i][row] = b[i]
for i in range(n):
  board[col][i] = a[i]
for i in board:
  print(''.join(i))