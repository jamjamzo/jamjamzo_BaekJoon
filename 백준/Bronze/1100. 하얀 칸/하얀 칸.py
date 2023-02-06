chess = []
for _ in range(8):
  chess.append(input())


even = 0
odd = 0
for i in range(8):
  for j in range(8):
    if i % 2 == 0:
      if j % 2 == 0:
        if chess[i][j] == 'F':
          even += 1
    elif i % 2 != 0:
      if j % 2 != 0:
        if chess[i][j] == 'F':
          odd += 1

print(even + odd)