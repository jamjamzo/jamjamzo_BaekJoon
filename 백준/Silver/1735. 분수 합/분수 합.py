def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)

a,b = map(int, input().split())
c,d = map(int,input().split())
e,f = ((a*d)+(b*c)), b*d
# print(e,f)

print(e//gcd(e,f),f//gcd(e,f))