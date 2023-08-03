n,w,h=map(int,input().split())
for i in range(n):
    m=int(input())
    z=((w*w)+(h*h))**0.5
    if z>=m:
        print('DA')
    else:
        print('NE')