# 방법1

sentence = input().lower()
code = input().lower()

# 알파벳 소문자 리스트, alpha[0] == ' '(공백)
alpha = [' ']
for i in range(97,123):
  alpha.append(chr(i))

def CodePrint(sentence, code):

  # 평문 - 숫자 변환
  sList = []
  for i in range(0,len(sentence)):
    sList.append(alpha.index(sentence[i]))
  
  # 암호키 - 숫자 변환
  cList = []
  i = 0
  while len(cList) != len(sList):
    cList.append(alpha.index(code[i%len(code)])) # 암호키의 길이가 평문보다 작을 수 있으니
    i += 1
  
  # 평문-암호키 뺀 값
  qList = []
  for i in range(len(sList)):
    #뺀 값이 양수
    if sList[i] > cList[i]:
      qList.append(sList[i]-cList[i])
    else:
      #공백
      if sList[i] == 0:
        qList.append(0)
      #뺀 값이 음수
      else:
        qList.append(26+(sList[i]-cList[i]))
  
  return qList


qList = CodePrint(sentence,code)

for i in qList:
  print(alpha[i], end='')