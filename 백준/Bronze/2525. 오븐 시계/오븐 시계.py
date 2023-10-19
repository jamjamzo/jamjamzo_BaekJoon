a, b = map(int, input().split())
t = int(input())

hour = (a*60+b+t)//60
if (hour>23):
  hour = hour - 24
minute = (a*60+b+t)%60

print(hour, minute)