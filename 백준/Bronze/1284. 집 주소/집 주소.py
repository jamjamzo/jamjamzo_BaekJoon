# 120 -> 1-2-0 (사이 2개) / -120- (양끝두개) / 숫자당차지하는공백 -**-***-****- (총 13개)
# 0 : ****
# 1 : **
# 2~9 : ***

while True:
  n = int(input())

  if n == 0:
    break

  else:
    n = list(str(n))
    blank = len(n) + 1 # 기본값 : 숫자 사이 공백(n자리수-1) + 맨 왼,오른쪽 공백 2개
    for i in n:
      if i == '1':
        blank += 2
      elif i == '0':
        blank += 4
      else:
        blank += 3

    print(blank)
  
  