num = int(input())
arr = []
for i in range(num):
    A, B = input().split()
    A = int(A)
    B = int(B)
    arr.append(A+B)
for i in arr:
    print(i)