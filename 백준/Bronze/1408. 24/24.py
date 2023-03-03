nh, nm, ns = map(int, input().split(':'))
mh, mm, ms = map(int, input().split(':'))

fSec = (mh* 3600 + mm*60 + ms) - (nh*3600 + nm*60 + ns)

if fSec < 0:
  fSec += 60*60*24

# second => hh:mm:ss 바꾸기
hour = fSec//3600
minute = (fSec%3600)//60
second = fSec%60

print("{}:{}:{}".format(str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2)))

