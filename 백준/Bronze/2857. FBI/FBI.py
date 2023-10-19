fbi = []
for i in range(5):
  b = input()
  if 'FBI' in b:
    fbi.append(i+1)
if fbi == []:
  print('HE GOT AWAY!')
else:
  print(*fbi, sep=' ')