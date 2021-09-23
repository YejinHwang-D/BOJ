word = list(input())
arr = [0]*26
for i in word:
    temp = ord(i)
    if 65<=temp & temp<=90:
        #대문자
        arr[temp-65] += 1;
    elif 97<=temp & temp<=122:
        #소문자
        arr[temp-97] += 1;
    else:
        break
max_value = max(arr)
cnt = arr.count(max_value)
if cnt>=2:
    print("?")
else:
    print(chr(arr.index(max_value)+65))