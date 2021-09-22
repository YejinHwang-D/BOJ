s = list(input())
for i in range(97, 123):
	i = chr(i)
	if i in s:
		loc = s.index(i)
		print(loc, end=' ')
	else:
		print(-1, end=' ')