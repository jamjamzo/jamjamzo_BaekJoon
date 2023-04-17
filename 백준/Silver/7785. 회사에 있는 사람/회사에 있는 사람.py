import sys 
input = sys.stdin.readline
enter = set()
for _ in range(int(input())):
  people = list(input().split())
  if people[1] == 'enter':
    enter.add(people[0])
  else:
    enter.remove(people[0])
enterList = sorted(list(enter), reverse=True)
print(*enterList, sep='\n')