# 처음 심어져 있는 가로수 수
n = int(input())

# 처음 시작값
a = int(input())

# 가로수 사이 값 저장
d = []
for i in range(n-1):
  b = int(input())
  d.append(b-a)
  a = b

# 최대공약수
def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)

# 최대공약수 찾기
g = d[0]
for j in range(1, len(d)):
  g = gcd(g,d[j])

# 둘 사이에 심을 가로 개수: (간격 // 최대공약수) -1
result = 0
for k in d:
  result += k//g -1 
print(result)