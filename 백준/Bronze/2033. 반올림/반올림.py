n = int(input())
d = 10
while n > d:
  if n % d >=  d//2:
    # ex) 15 % 10 = 5 (>=) 5
    n += d
    # 15+10 = 25
  n -= (n%d) 
  # 25-5
  d *=10
  # 100
print(n)
