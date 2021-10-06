a, b, v = map(int, input().split())
# 시간 = 거리/속력
day = (v-a)/(a-b)+1
if day%1!=0:
    #소수점이면
    day = int(day)+1
print(int(day))