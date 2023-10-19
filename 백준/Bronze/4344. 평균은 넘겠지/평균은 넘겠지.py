c = int(input()) # 테스트 케이스의 개수
for i in range(c):
  info = list(map(int, input().split()))
  student = info[0]
  score = info[1:len(info)]
  average = sum(score) / student
  over_avg = 0
  for j in score:
    if j > average:
      over_avg +=1
  print(format(over_avg/student*100,".3f"),"%")