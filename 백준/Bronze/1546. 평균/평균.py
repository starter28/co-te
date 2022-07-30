import sys

input = sys.stdin.readline
score_cnt = int(input().rstrip())
score = list(map(int, input().split()))
max_val = max(score)

for i in range(score_cnt):
	score[i] = score[i] / max_val * 100
print(sum(score) / len(score))
	