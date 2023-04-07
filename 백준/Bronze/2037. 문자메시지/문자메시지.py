key = [[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
p, w = map(int, input().split())
text = input()
time = 0
check = ''
for i in range(len(text)):
  if text[i] == ' ':
    time += p
    check = ''
  
  for j in range(len(key)):
    for k in range(len(key[j])):
      if text[i] == key[j][k]:
        if j == check:
          time += w
        time += (1+k)*p
        check = j

print(time)