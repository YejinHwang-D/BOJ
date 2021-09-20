def d(n):
	temp=n
	while(temp!=0):
		arr.append(temp%10)
		temp=temp//10
	compare.append(n+sum(arr))

compare = []
for i in range(1,10001):
    arr=[]
    d(i)
    
for i in range(1,10001):
    if i not in compare:
        print(i)