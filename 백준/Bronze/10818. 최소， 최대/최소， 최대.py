import sys

input = sys.stdin.readline
num_cnt = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))
	