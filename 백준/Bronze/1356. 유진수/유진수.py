# 유진수: 어떤 수를 10진수로 표현
# 1221 -> 1*2 == 2 * 1 (ok)
# 1236 -> 1*2*3 == 6 (ok)
# 1234 -> (x)
# 2 자리 이상

n = list(map(int, input()))
nLen = len(n)

if nLen == 1:
  print('NO')

else:
  a = b = 1
  for i in range(nLen - 1):
    a = b = 1
    for j in range(i + 1):
      a *= n[j]
    
    for k in range(i+1,nLen):
      b *= n[k]

    if a == b:
      break

  if a == b:
    print('YES')
  else:
    print('NO')
