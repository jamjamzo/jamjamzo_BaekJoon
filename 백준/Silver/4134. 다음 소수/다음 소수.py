def is_prime_num(x):
  if x == 0 or x == 1:
    return False
  for i in range(2,int(x**0.5)+1):
    if x % i == 0:
      return False # 소수가 아님
  return True # 소수임

for _ in range(int(input())):
  n = int(input())

  while True:
    if n == 0 or n == 1:
      print(2)
      break
    if is_prime_num(n):
      print(n)
      break
    else:
      n += 1
