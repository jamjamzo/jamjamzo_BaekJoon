# g: 좋은놈
# b: 나쁜놈

for _ in range(int(input())):
  word = input()
  word_lower = word.lower()

  g = word_lower.count('g')
  b = word_lower.count('b')

  if g > b:
    print(f"{word} is GOOD")
  elif g < b:
    print(f"{word} is A BADDY")
  else:
    print(f"{word} is NEUTRAL")