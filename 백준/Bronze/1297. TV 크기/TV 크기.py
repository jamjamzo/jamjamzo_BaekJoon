d, h, w = map(int, input().split())
x = d/(h**2+w**2)**0.5
print(int(h*x),int(w*x))