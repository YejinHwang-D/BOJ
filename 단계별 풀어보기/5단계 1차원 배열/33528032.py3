n=int(input())
score_arr=[]

for i in range(n):
    score=1
    sum=0
    test = list(input()) #각 case list 입력받기
    for j in test:
        if j=='O':
            sum+=score
            score+=1
        else:    #만약 X를 만나면 연속 점수 초기화
            score=1
    score_arr.append(sum)

for i in score_arr:
    print(i)