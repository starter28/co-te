import sys

input = sys.stdin.readline
num = int(input().rstrip()) * int(input().rstrip()) * int(input().rstrip())
num_str = str(num)

print(num_str.count('0'), num_str.count('1'), num_str.count('2'), \
num_str.count('3'), num_str.count('4'), num_str.count('5'), \
num_str.count('6'), num_str.count('7'), num_str.count('8'), \
num_str.count('9'), sep='\n')