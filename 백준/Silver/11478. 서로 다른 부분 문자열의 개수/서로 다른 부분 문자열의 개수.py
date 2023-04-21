S = input()
s_set = set()
for i in range(len(S)):
  for j in range(i,len(S)):
    s_set.add(S[i:j+1])
    
print(len(s_set))