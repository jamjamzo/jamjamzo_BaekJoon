def prime_num(n):
  if n == 1:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

all_num = list(range(1,246912))

prime_list = []
for i in all_num:
  if prime_num(i):
    prime_list.append(i)

n = int(input())
while True:
  cnt = 0
  if n == 0:
    break
  for i in prime_list:
    if i > n and i <= 2*n:
      cnt += 1
  print(cnt)
  n = int(input())