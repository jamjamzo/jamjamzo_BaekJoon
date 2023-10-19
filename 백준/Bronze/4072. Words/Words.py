# 방법1
while True:
  words = list(input().split())
  if (len(words) == 1) and (words[0] == '#'):
    break

  for w in words:
    print(w[::-1], end = ' ')
  print()