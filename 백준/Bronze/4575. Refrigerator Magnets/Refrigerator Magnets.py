while True:

  s1 = input()

  if s1 == 'END':
    break

  s1_list = list(s1.replace(' ',''))
  s1_set = set(s1_list)

  if len(s1_list) == len(s1_set):
    print(s1)