import sys
arr = []
T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append(a+b)
for i in arr:
    print(i)
