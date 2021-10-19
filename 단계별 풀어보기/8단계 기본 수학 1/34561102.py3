N = int(input())
bag3 = 0
bag5 = 0
current = N
while current>=0:
    if current%5==0: #5의 배수이면
        bag5 += current//5
        break
    else:
        #5의 배수가 아니면
        bag3 += 1
        current -= 3
if current<0:
    print(-1)
else:
    print(bag3+bag5)