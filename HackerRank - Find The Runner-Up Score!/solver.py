# Find the Runner-Up Score!

n = int(input())
score = [x for x in map(int, input().split())]

score = list(set(score))
score.sort()
print(score[-2])