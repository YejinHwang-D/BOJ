arr = []
max = 0
sum = 0
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
	if i>max:
		max=i
for i in range(n):
    arr[i] = arr[i]/max*100
    sum += arr[i]
print(sum/n)