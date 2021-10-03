n = int(input())
cnt = 0
for i in range(1, 2000002):
    cnt += i
    if n<=cnt:
        temp = cnt-n
        if i%2==0:
            print("%d/%d" % (i-temp, temp+1))
            break
        else:
            print("%d/%d" % (temp+1, i-temp))
            break