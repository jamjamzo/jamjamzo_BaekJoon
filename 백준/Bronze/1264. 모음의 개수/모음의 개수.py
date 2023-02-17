vowels = ['a','e','i','o','u']
while True:
  sentence = input()
  if sentence == '#':
    break
  else:
    sentence = list(sentence.lower().replace(" ",""))
    vowel_cnt = 0
    for v in vowels:
      if v in sentence:
        vowel_cnt += sentence.count(v)
    print(vowel_cnt)
  