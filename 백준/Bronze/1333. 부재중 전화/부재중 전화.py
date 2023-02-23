n, l, d = map(int, input().split())

album = [True]*(n * l + 5 * (n-1)) # 총 00초: 1초당 False지정

# 앨범 수록곡 수만큼 for문
for i in range(n):
  s = (l+5) * i # 0초부터 시작
  # 범위(한 곡이 마치고, 다음 곡이 재생되기 전)
  for j in range(s,s+l):
    album[j] = False # 노래 구간만 True

call = 0
while call < len(album):
  # if not: False이면 실행
  # album[call] == False 이면 Break
  if album[call]:
    break
  call += d
print(call)