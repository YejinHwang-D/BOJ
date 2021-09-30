n = int(input())
cnt = 1
num = 1
if n!=1:
    while n > num:
        num += 6*cnt
        cnt += 1
print(cnt)