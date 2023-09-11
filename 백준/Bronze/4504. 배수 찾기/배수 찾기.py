n = int(input())
while True:
  w = int(input())
  if w == 0:
    break
  if w % n == 0:
    print(f"{w} is a multiple of {n}.")
  else:
    print(f"{w} is NOT a multiple of {n}.")