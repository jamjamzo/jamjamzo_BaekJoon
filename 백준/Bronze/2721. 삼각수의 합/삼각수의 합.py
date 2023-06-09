# 방법1
def t(n):
  hap = 0
  for i in range(1,n+1):
    hap += i
  return hap

def w(n):
  hap = 0
  for i in range(1,n+1):
    hap += (i*t(i+1))
  return hap

for _ in range(int(input())):
  n = int(input())
  print(w(n))