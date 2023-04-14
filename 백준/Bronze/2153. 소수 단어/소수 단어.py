# 첫번째방법
def TextNumber(text):
  alpha = [' ']
  for i in range(97,123):
    alpha.append(chr(i))
  for i in range(65,91):
    alpha.append(chr(i))
  n = 0
  for i in range(len(text)):
    a = alpha.index(text[i])
    n += a
  return n

text = input()
x = TextNumber(text)
y = 1
cnt = 0
while y <= x:
  if x % y == 0:
    cnt += 1
  y+= 1

if cnt <= 2:
  print('It is a prime word.')
else:
  print('It is not a prime word.')
