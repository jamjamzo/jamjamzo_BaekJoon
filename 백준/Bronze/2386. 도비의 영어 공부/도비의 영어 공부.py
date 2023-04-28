# 방법2
while True:
  s = input()
  if s == '#':
    break
  a = s[0]
  b = s[2:].lower()
  print(a,b.count(a))