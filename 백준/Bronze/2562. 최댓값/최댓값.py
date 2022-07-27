import sys

input = sys.stdin.readline
num_arr = []
i_max = 0

for i in range(9):
	num_arr.append(int(input().rstrip()))
	if num_arr[i_max] < num_arr[i]:
		i_max = i
print(num_arr[i_max], i_max + 1, sep='\n')