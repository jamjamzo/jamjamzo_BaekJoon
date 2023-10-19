croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in range(len(croatia)):
  if croatia[i] in word:
    word = word.replace(croatia[i],'&')

print(len(word))