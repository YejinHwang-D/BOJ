def calc(n):
	temp=n
	length=len(str(n))
	if length <=2:
		return "o"
	else:
		while (temp!=0):
			arr.append(temp%10)
			temp=temp//10
		for i in range(0, len(arr)-2):
			if arr[i]-arr[i+1] != arr[i+1]-arr[i+2]:
				return "x"
		return "o"
        
cnt = 0
n = int(input())
for i in range(1, n+1):
    arr = []
    if calc(i)=='o':
        cnt+=1
print(cnt)