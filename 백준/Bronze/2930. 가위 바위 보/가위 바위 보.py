def check(a,b):
  if a == 'S':
    if b == 'S':
      return 1
    if b == 'P':
      return 2
    if b == 'R':
      return 0
  if a == 'P':
    if b == 'S':
      return 0
    if b == 'P':
      return 1
    if b == 'R':
      return 2
  if a == 'R':
    if b == 'S':
      return 2
    if b == 'P':
      return 0
    if b == 'R':
      return 1

r = int(input()) # 몇판게임인지
me = input() # 내가 낸 가위바위보
n = int(input()) # 친구 몇명
oppo = [input() for _ in range(n)]

score = 0
max_score = 0

for i in range(r):
  max_list = [0,0,0]
  for j in range(n):
    score += check(me[i],oppo[j][i])

    max_list[0] += check('S',oppo[j][i])
    max_list[1] += check('P',oppo[j][i])
    max_list[2] += check('R',oppo[j][i])
  max_score += (max(max_list))


print(score) # 최종스코어
print(max_score) # 전부 이겼다고 가정했을때
