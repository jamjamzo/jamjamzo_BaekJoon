def d(n):
  n = n + sum(map(int, str(n)))
  return n

num_set = set()
for i in range(1,10001):
  num_set.add(d(i))

for i in range(1,10001):
  if i not in num_set:
    print(i)