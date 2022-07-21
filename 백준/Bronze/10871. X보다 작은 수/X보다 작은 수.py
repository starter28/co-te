import sys

input = sys.stdin.readline
num_cnt, num_find = map(int, input().split())
num_str = list(map(int, input().split()))
result = ""

for i in range(num_cnt):
	if (num_str[i] < num_find):
		result += (str(num_str[i]) + " ")
print(result)