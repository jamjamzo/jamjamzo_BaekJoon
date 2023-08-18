t = int(input())
for _ in range(t):
  x = 0
  y = 0
  while True:
    a = input()
    if a == '':
      break
    else:
      x += len(a)
      y += len(a) - a.count('#')
  z = round((y/x)*100,1)

  if z % 1 == 0:
    print('Efficiency ratio is {}%.'.format(int(z)))
  else:
    print('Efficiency ratio is {}%.'.format(z))