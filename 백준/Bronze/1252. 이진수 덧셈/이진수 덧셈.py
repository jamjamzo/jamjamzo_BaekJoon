a,b = map(str, input().split())
c = bin(int(a,2) + int(b,2))
print(c[2:])