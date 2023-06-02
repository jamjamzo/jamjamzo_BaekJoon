# 방법 1
# import sys
# input = sys.stdin.readline
rule = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for _ in range(int(input())):
  rule_cnt = [0 for _ in range(8)]
  coin = input()
  for i in range(1,len(coin)-1):
    a = coin[i-1:i+2]
    if a in rule:
      rule_cnt[rule.index(a)] += 1

  print(*rule_cnt, sep= ' ')
  