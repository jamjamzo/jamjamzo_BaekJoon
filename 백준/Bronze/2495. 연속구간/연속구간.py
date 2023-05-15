for i in range(3):
  text = input()
  cMax = 1
  cnt = 1
  for i in range(1,len(text)):
    if text[i] == text[i-1]:
      cnt += 1
    else:
      cMax = max(cnt, cMax)
      cnt = 1
  cMax = max(cnt,cMax)
  print(cMax)
      