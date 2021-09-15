n = int(input())
arr = list(map(int, input().split()))
min = 1000000
max = -1000000
for i in arr:
    if (i < min):
        min = i
    if (i > max):
        max = i
print(min, max)