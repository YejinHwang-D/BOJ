#1로 시작해서 1로 줄어야 한다.
#(1, 2) (3, 3, 4, 4) (5, 5, 5, 6, 6, 6) (7, 7, 7, 7, 8, 8, 8, 8) 
#1 1 2 2 3 3 4 4 5 5 6 6 < 반복 횟수
#2, 6, 12, 20은 1*2, 2*3, 3*4, 4*5 => n*(n+1)
#제곱근 2, 4, 9, 16 기준으로 아래 위 분리
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    dist = y-x
    cnt = 0
    
    while dist > cnt*(cnt+1):
        cnt+=1
    if dist <= cnt**2:
        print(cnt*2-1)
    else:
        print(cnt*2)