a, b = map(int, input().split())
a = a-1
b = b-1

print(abs(b//4-a//4)+abs(b%4-a%4))