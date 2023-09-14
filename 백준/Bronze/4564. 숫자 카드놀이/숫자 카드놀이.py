while True:
  s = input()
  if s == '0':
    break
  print(s, end=' ')
  if len(s) == 1:
    print()
    continue
  else:
    while True:
      result = 1
      for i in s:
        result *= int(i)
      print(result, end= ' ')
      s = str(result)
      if len(s) == 1:
        break
  print()