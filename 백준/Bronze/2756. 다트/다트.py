def score(x,y):
  d = x**2+y**2
  xy_score = 0
  if d <= 9:
    xy_score = 100
  elif d <= 36:
    xy_score = 80
  elif d <= 81:
    xy_score = 60
  elif d <= 144:
    xy_score = 40
  elif d <= 225:
    xy_score = 20
  else:
    xy_score = 0
  return xy_score


for _ in range(int(input())):
  a = list(map(float, input().split()))
  n = a[:6]
  m = a[6:]

  n_score = 0
  m_score = 0
  for i in range(0,6,2):
    n_score += score(n[i],n[i+1])
    m_score += score(m[i],m[i+1])

  if n_score > m_score:
    print('SCORE: {} to {}, PLAYER 1 WINS.'.format(n_score,m_score))
  elif n_score < m_score:
    print('SCORE: {} to {}, PLAYER 2 WINS.'.format(n_score,m_score))
  else:
    print('SCORE: {} to {}, TIE.'.format(n_score,m_score))
