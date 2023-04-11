end1 = [31,28,31,30,31,30,31,31,30,31,30,31] # 평년
end2 = [31,29,31,30,31,30,31,31,30,31,30,31] # 윤년
yun = []
for year in range(1700, 2201):
  if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    yun.append(year)
  elif year % 4 == 0 and year % 100 != 0:
    yun.append(year)

while True:
  d,m,y = map(int,input().split())
  if d == 0 and m == 0 and y == 0:
    break
  if y in yun:
    days = 0
    
    for i in range(m-1):
      days += end2[i]
    
    days = days + d
    print(days)

  else:
    days = 0
    for i in range(m-1):
      days += end1[i]
    days = days + d
    print(days)
