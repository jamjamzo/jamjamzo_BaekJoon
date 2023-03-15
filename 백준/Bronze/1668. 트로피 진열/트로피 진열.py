def ascending(array):
    now = array[0]
    result = 1
    for x in range(1, len(array)):
        if now < array[x]:
            result += 1
            now = array[x]
    return result

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))