n = int(input())
s = list(input())
table = {'AA':'A','AG':'C','AC':'A','AT':'G',
         'GA':'C','GG':'G','GC':'T','GT':'A',
         'CA':'A','CG':'T','CC':'C','CT':'G',
         'TA':'G','TG':'A','TC':'G','TT':'T'}

while True:
  if len(s) == 1:
    break

  code = s[-2] + s[-1]
  if code in table:
    del s[-2:]
    s.append(table.get(code))

print(*s)