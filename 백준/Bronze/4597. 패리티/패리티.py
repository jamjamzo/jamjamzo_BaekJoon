#e: 짝수, o: 홀수
while True:
  s = input()
  if s == '#':
    break

  end = s[-1]
  s = s[:-1]
  # print(end, s)

  cnt_1 = s.count('1')
  # print(cnt_1)

  if end == 'e':
    if cnt_1 % 2 == 0:
      end = '0'
    else:
      end = '1'
  else:
    if cnt_1 % 2 == 0:
      end = '1'
    else:
      end = '0'

  print(s + end)
