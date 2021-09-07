h, m = input().split()
h = int(h)
m = int(m)
if m>=45:
    m = m-45
    print(h, m)
else:
    #result_m + 45 = 60 + m
    if h!=0:
        h = h-1
    else:
        h = 23
    m = 15+m
    print(h, m)