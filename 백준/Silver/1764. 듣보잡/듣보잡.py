n,m = map(int,input().split())
NotListen = set()
for _ in range(n):
  NotListen.add(input())
NotWatch = set()
for _ in range(m):
  NotWatch.add(input())

NOT = list(NotListen & NotWatch) # list(set() & set()) : 교집합
NOT.sort()

print(len(NOT))
print(*NOT, sep='\n')