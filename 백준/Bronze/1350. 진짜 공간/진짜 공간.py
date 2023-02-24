n = int(input())
size = list(map(int, input().split()))
default = int(input())

total = []
for i in range(len(size)):
  if size[i] == 0:
    total.append(0)
  else:
    if size[i] / default <1:
      total.append(default)
    else:
      if size[i] % default == 0:
        total.append(default*(size[i]//default))
      else:
        total.append(default*(size[i]//default +1))
print(sum(total))
    

