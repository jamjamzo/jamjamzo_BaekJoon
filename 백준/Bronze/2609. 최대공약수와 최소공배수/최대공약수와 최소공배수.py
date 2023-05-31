# 방법2
def cal(a,b):
  if b == 0:
    return a
  if a % b == 0:
    return b
  return cal(b, a%b)

n,m = map(int, input().split())
a,b = max(n,m), min(n,m)
# 최대공약수
print(cal(a,b))
print((a*b) // cal(a,b))