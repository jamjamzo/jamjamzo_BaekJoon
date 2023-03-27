code = {'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}

while True:
  a = input()
  if a == '#':
    break
  
  else:
    b = len(a) # 자릿수
    x = 0
    for i in range(b):
      x += code[a[i]] * (8**(b-1-i))
      
    print(x)