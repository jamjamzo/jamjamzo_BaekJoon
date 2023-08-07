# 방법2
numbers = sorted(list(map(int, input().split())))
words = input()

for w in words:
  if w == 'A':
    print(numbers[0], end= ' ')
  elif w == 'B':
    print(numbers[1], end= ' ')
  else:
    print(numbers[2], end= ' ')