def gandalf(lst):
  score = [1,2,3,3,4,10]
  total = 0
  for i in range(6):
    total += lst[i] * score[i]
  return total

def sauron(lst):
  score = [1,2,2,2,3,5,10]
  total = 0
  for i in range(7):
    total += lst[i] * score[i]
  return total

for i in range(1,int(input())+1):
  a = gandalf(list(map(int, input().split())))
  b = sauron(list(map(int, input().split())))
  # print(a, b)

  if a > b:
    print(f"Battle {i}: Good triumphs over Evil")
  elif a < b:
    print(f"Battle {i}: Evil eradicates all trace of Good")
  else:
    print(f"Battle {i}: No victor on this battle field")
