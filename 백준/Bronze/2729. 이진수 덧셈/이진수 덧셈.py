for _ in range(int(input())):
  x, y = input().split()
  a = int(x,2)
  b = int(y,2)
  print(bin(a+b)[2:])