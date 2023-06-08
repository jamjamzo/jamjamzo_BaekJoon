c = [25,10,5,1]
t = int(input())
for _ in range(t):
  n = int(input())
  x = []

  for i in c:
    x.append(n//i)
    n = n % i 
  print(*x)