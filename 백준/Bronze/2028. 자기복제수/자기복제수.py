# 방법2
def dup(num):
    if str(num**2)[-len(str(num)):] == str(num):
        return "YES"
    return "NO"
for i in range(int(input())):
    print(dup(int(input())))