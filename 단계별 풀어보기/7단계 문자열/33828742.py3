arr = input()
temp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in temp:
    if i in arr:
        arr = arr.replace(i, " ")
print(len(arr))