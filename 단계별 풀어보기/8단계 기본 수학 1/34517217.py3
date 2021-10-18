T = int(input())
for i in range(T):
    arr = []
    k = int(input()) #층
    n = int(input()) #호수
    for j in range(n): #0층 사람 수 추가
        arr.append(j+1)
    for j in range(k): #층 올라갈 때마다 반복
        for u in range(1, n): #호수 체크
            arr[u] += arr[u-1] #전 호수 수 더해가기
            print
    print(arr[n-1])           