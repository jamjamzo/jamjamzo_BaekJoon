while True:
  n = int(input())
  if n == -1:
    break
  names = []
  clay = []
  for i in range(n):
    a,b,c,name = input().split()
    names.append(name)
    clay.append(int(a)*int(b)*int(c))
  print(f"{names[clay.index(max(clay))]} took clay from {names[clay.index(min(clay))]}.")

