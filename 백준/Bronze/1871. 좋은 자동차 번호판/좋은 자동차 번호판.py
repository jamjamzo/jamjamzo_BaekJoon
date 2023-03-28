for _ in range(int(input())):
  a, b = input().split('-')
  b = int(b)

  n = 0
  for i in range(3):
    n+= (ord(a[i])-65)*(26**(2-i))
  
  if abs(n-b) <= 100 :
    print("nice")
  else:
    print("not nice")