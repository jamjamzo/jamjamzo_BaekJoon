# ord("A"), ord("Z") # 65 90

for _ in range(int(input())):
  a,b = input().split()
  a = int(a)
  c = ord(b)

  for i in range(a):
    d = c + i
    if d <= 90:
      print(chr(d)*(i+1))
    else:
      print(chr(d-90+64)*(i+1))
  print()