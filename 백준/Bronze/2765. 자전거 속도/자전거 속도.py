# 지름(인치), 회전수, 시간
pi = 3.1415927
n = 1
while True:
  a,b,c = map(float, input().split())
  # 회전수가 0이면 중지
  if b == 0:
    break

  # inch -> mile 변경
  distance = a/(5280*12) *pi*b
  # second -> hour 변경
  mph = distance/c *3600
  print('Trip #%d: %.2f %.2f' %(n,distance,mph))
  n += 1