import sys

input = sys.stdin.readline
num_list = []

while 1:
	num_list = list(input())
	if not num_list:
		break
	print(int(num_list[0]) + int(num_list[2]))