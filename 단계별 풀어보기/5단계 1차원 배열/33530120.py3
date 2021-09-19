n = int(input())
for i in range(n):
    cnt=0
    scores = list(map(int,input().split()))
    student = scores[0]
    avg = (sum(scores)-student)/student
    for j in range(1, student+1):
        if scores[j] > avg:
            cnt += 1
    print("{:.3f}%".format(cnt/student*100))