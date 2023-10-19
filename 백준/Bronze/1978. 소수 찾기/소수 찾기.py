

# 소수: 1과 자기 자신만 있는 자연수
n = int(input())
a = list(map(int, input().split()))

# 나머지가 0인 수를 모두 카운트할 때, 카운트 개수가 1개만 있는 원소만을 prime으로 더한다. 
prime= 0
for i in a:
    cnt = 0
    if i > 1:
        for j in range(2,i+1):
            if i%j == 0:
                cnt += 1 
        if cnt == 1:
            prime += 1

print(prime)