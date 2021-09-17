a = int(input())
b = int(input())
c = int(input())
result = a*b*c
cnt = [0,0,0,0,0,0,0,0,0,0]
while (result!=0):
    what = result%10
    cnt[what] += 1
    result = result//10
for i in cnt:
    print(i)