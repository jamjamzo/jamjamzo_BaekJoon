n = int(input())
player_list = sorted([input()[0] for i in range(n)])
player_set = set(player_list)
result = []
for i in player_set:
  if player_list.count(i) >= 5:
    result.append(i)

if len(result) > 0:
  print(''.join(sorted(result)))
else:
  print('PREDAJA')