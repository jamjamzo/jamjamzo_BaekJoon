score = [int(input()) for _ in range(10)]
answer = 0
i = 0
while i <= 9:
  answer += score[i]
  if answer == 100:
    break
  elif answer > 100:
    if answer - 100 <= 100 - (answer-score[i]):
      break
    else:
      answer = answer - score[i]
    break
  i += 1
print(answer)