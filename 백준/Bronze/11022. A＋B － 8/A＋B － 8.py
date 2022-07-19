import sys
 
input = sys.stdin.readline
t_cnt = int(input())
 
for i in range(t_cnt):
	num1, num2 = map(int, input().split())
	print("Case #%s: %d + %d = %d"%(i+1, num1, num2, num1+num2))