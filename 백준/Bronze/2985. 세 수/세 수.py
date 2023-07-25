a,b,c = map(int,input().split())

# 덧셈
if a + b == c:
  print('{}+{}={}'.format(a,b,c))
elif b + c == a:
  print('{}={}+{}'.format(a,b,c))
# 뺄셈
elif a - b == c:
  print('{}-{}={}'.format(a,b,c))
elif b - c == a:
  print('{}={}-{}'.format(a,b,c))
# 곱셈
elif a * b == c:
  print('{}*{}={}'.format(a,b,c))
elif b * c == a:
  print('{}={}*{}'.format(a,b,c))
# 나눗셈
elif a / b == c:
  print('{}/{}={}'.format(a,b,c))
elif b / c == a:
  print('{}={}/{}'.format(a,b,c))