def Game(a,b):
  # a: p1, b: p2
  x = y = 0
  if a == 'R' and b == 'P': y += 1
  elif a == 'P' and b == 'S': y += 1
  elif a == 'S' and b == 'R': y += 1
  elif a == 'P' and b =='R': x += 1
  elif a == 'S' and b =='P': x += 1
  elif a == 'R' and b =='S': x += 1
  return x,y

while True:
  p1 = list(input())
  p2 = list(input())

  if p1[0] == "E" and p2[0] == "E":
    break

  p1_score = p2_score = 0
  for i in range(len(p1)):
    x,y = Game(p1[i],p2[i])
    p1_score += x
    p2_score += y

  print(f"P1: {p1_score}")
  print(f"P2: {p2_score}")