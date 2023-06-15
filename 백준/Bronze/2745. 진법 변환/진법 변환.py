# 알파벳 추출
#  a = [chr(i) for i in range(65,91)]
#  print(*a,sep='')
nlist = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()
n = ''.join(reversed(n))
b = int(b)
res = 0
for i in range(len(n)-1,-1,-1):
  res += nlist.index(n[i]) * (b**i)
print(res)