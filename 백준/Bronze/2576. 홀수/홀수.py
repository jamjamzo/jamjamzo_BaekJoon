odd = []
for _ in range(7):
  o = int(input())
  if o%2 != 0:
    odd.append(o)
if odd == []:
  print(-1)
else:
  print(sum(odd))
  print(min(odd))