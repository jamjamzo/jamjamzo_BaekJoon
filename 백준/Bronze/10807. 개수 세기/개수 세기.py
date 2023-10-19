# n: 몇 개의 정수를 넣을 것인지
# m: 입력되는 정수들을 list형으로 변수 
# x: m에 들어가 있는 x값을 찾기 
n = int(input()) 
m = list(map(int, input().split()))
x = int(input())
print(m.count(x)) # m안에 x값이 몇개 들어있는지 개수 세기