import sys
import re
word = sys.stdin.readlines()
for i in word:
  while True:
    result = re.sub('BUG', '', i)
    if 'BUG' in result:
      i = result
    else:
      print(result, end='')
      break