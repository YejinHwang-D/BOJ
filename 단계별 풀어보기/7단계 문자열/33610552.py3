n = int(input())
for i in range(n):
    num, desc = input().split()
    desc = list(desc)
    num = int(num)
    for j in desc:
        for k in range(num):
            print(j, end='')
    print()