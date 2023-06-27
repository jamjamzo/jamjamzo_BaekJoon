n = int(input())
s = input()
couple = 0
for i in range(n):
  if s[i] == 'L':
    couple += 1
couple = couple // 2
print(min(n+1-couple,n))