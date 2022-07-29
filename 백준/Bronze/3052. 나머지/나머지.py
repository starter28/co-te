import sys

input = sys.stdin.readline
num_list = [0 for _ in range(10)]

for i in range(10):
	num_list[i] = (int(input().rstrip()) % 42)

num_set = set(num_list)
print(len(num_set))