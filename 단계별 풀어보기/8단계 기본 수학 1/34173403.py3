t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    f = n%h #층수
    if f==0:
        f = h
        room = n//h
    else:
        room = n//h+1 #방번호
    print(f*100 + room)