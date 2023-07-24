# 방법1
a,b,c = list(map(int, input().split()))
park = [0]*100
for _ in range(3):
  x,y = map(int, input().split())
  for i in range(x,y):
    park[i] += 1

res = 0
for j in park:
  if j == 1:
    res += a
  elif j == 2:
    res += (b*2)
  elif j == 3:
    res += (c*3)
  else:
    res += 0
print(res)