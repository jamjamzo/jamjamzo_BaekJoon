import sys

def init_tree(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(node * 2, start, mid) + init_tree(node * 2 + 1, mid + 1, end)
    return tree[node]

def update_tree(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, idx, diff)
        update_tree(node * 2 + 1, mid + 1, end, idx, diff)

def query_tree(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query_tree(node * 2, start, mid, left, right) + query_tree(node * 2 + 1, mid + 1, end, left, right)

N, M, K = map(int, sys.stdin.readline().split())
nums = [0] * (N + 1)
tree = [0] * (4 * N)

for i in range(1, N + 1):
    nums[i] = int(sys.stdin.readline())

init_tree(1, 1, N)

output = []
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - nums[b]
        nums[b] = c
        update_tree(1, 1, N, b, diff)
    else:
        result = query_tree(1, 1, N, b, c)
        output.append(str(result))

sys.stdout.write('\n'.join(output))
