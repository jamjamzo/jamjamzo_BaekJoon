unit = {'kg':2.2046,'lb':0.4536,'l':0.2642,'g':3.7854}
for _ in range(int(input())):
  a,b = input().split()
  if b == 'kg':
    print('{:.4f}'.format(float(a)*float(unit[b])),'lb')
  elif b == 'lb':
    print('{:.4f}'.format(float(a)*float(unit[b])),'kg')
  elif b == 'l':
    print('{:.4f}'.format(float(a)*float(unit[b])),'g')
  elif b == 'g':
    print('{:.4f}'.format(float(a)*float(unit[b])),'l')