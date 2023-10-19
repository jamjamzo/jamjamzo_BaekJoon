# 한마리당 쿠폰 n장 
# 치킨 한마리당 도장 - 도장 k개 : 쿠폰 1장
while True:
  try:
    n, k = map(int, input().split())
    chicken  = 0
    chicken += n
    while n//k:
      chicken += n//k
      n = n//k + n%k
    print(chicken)
  
  except:
    break