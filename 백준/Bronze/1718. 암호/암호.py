# 방법 2

sentence = input().lower()
code = input().lower()
a = ''
for i in range(len(sentence)):
  if sentence[i] == ' ':
    a += ' '
  
  else:
    b = ord(sentence[i])- ord(code[i%len(code)])
    
    if b > 0:
      a += chr(b+96)
    else:
      a += chr(b+96+26)

print(a)