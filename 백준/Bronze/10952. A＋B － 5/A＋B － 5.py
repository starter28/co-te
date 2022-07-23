import sys

input = sys.stdin.readline

while(1):
	num1, num2 = map(int, input().split())
	ret = num1 + num2
	if (ret == 0):
		break
	print(num1 + num2)