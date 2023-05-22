n,p = map(int, input().split())
a_list = []
a = n
while True:
  b = (n*a)%p
  if b in a_list:
    print(len(a_list)-a_list.index(b))
    break
  a_list.append(b)
  a = b 