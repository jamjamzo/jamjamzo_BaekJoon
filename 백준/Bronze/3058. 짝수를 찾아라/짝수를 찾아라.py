for t in range(int(input())):
  numbers = sorted(list(map(int, input().split())))
  even = []
  for n in numbers:
    if n % 2 == 0:
      even.append(n)
  print(sum(even), even[0])
  # print(sum(even), min(even))