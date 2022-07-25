import sys

input = sys.stdin.readline
input_val = input().rstrip()
cal_val = input_val
cnt = 0

if len(cal_val) == 1:
	cal_val = '0' + cal_val

while 1:
	ret_val = str(int(cal_val[0]) + int(cal_val[-1]))
	cal_val = cal_val[-1] + ret_val[-1]
	cnt += 1
	if int(input_val) == int(cal_val):
		break
print(cnt)