score = []
for _ in range(5):
  a = list(map(int, input().split()))
  score.append(sum(a))
print(score.index(max(score))+1, max(score))
