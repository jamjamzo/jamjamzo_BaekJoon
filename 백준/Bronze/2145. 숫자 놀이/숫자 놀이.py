while True:
  n = input()
  if int(n) == 0:
    break

  while len(n) != 1:
    a = 0
    for i in range(len(n)):
      a += int(n[i])
    n = str(a)

  print(n)

# str(sum(list(map(int, n))))