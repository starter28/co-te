import sys

input = sys.stdin.readline
line_cnt = int(input())

for i in range(1, line_cnt + 1):
	print(' ' * (line_cnt - i) + '*' * i)