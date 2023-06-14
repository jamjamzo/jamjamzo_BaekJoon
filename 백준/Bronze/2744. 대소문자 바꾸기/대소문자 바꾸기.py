letter = input()
new = ''
for i in range(len(letter)):
  if letter[i].islower():
    new += letter[i].upper()
  else:
    new += letter[i].lower()
print(new)