# 방법1
while True:
  s = list(input().split())
  a = s[0]
  if a == '#':
    break
  
  cnt = 0
  for i in range(1, len(s)):
    cnt += s[i].lower().count(a)
  print(a, cnt)