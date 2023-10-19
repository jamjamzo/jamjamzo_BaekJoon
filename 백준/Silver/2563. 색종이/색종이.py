arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            arr[row][col] = 1
total = 0
for i in arr:
    total += sum(i)
print(total)