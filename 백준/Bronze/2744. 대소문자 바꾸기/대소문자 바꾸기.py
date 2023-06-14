new = ''
for i in input():
  if i.islower():
    new += i.upper()
  else:
    new += i.lower()
print(new)