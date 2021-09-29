a, b, c = map(int, input().split())
#식은 n >= a/(c-b)
if b>=c:
    print(-1)
else:
    n = a//(c-b)
    print(n+1)
    


