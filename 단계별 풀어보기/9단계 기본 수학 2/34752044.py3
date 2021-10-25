N = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in arr:
    temp = 0
    for j in range(1, i+1):
        if i%j==0: #수가 나누어 떨어지면
            temp+=1
    if temp==2: #1과 자기 자신만
        cnt+=1
print(cnt)