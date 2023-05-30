line = []
n = int(input())
ticket = list(map(int, input().split()))

for i in range(n):
  line.insert(ticket[i],i+1)
print(*line[::-1])